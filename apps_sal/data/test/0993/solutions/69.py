from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0]
for i in range(n):
    l.append(a[i] + l[i])
for i in range(n + 1):
    l[i] %= m
c = Counter(l)
ans = 0
for i in c.values():
    ans += i * (i - 1) // 2
print(ans)
