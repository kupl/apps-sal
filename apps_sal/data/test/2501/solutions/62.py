from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = []
c = []
ans = 0
for i, j in enumerate(a):
    b.append(i + j)
    c.append(i - j)
d = Counter(c)
for i in b:
    ans += d.get(i, 0)

print(ans)
