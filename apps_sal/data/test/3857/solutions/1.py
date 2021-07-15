from bisect import bisect_left
input()
s = []
for i in sorted(map(int, input().split())):
    k = bisect_left(s, -i)
    if k == len(s): s.append(-1)
    else: s[k] -= 1
print(len(s))
