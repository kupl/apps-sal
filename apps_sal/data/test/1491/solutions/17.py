from bisect import bisect_left
sq = [i * i for i in range(10**5 + 5)]
a = []
nules = 0
ap = a.append
n = int(input()) // 2
for i in map(int, input().split()):
    if i == 0:
        ap(0)
        nules += 1
    else:
        ind = bisect_left(sq, i)
        ap(min(i - sq[ind - 1], sq[ind] - i))
a = sorted(a)
s = sum(a[:n])
if s == 0:
    print(n - a[::-1].index(0) + max(0, nules - n))
else:
    print(s)
