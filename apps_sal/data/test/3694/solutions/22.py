ans = ["sjfnb", "cslnb"]
n = int(input())
l = list(map(int, input().split()))
l.sort()
d = set()
e = 0
s = 0
for i in range(n):
    if l[i] in d:
        e += 1
        s = l[i]
    d.add(l[i])
if e > 1 or l.count(0) > 1 or s - 1 in d:
    print(ans[1])

else:
    l = [l[i] - i for i in range(n)]
    # print(l)
    print(ans[1 - sum(l) % 2])
