from math import gcd
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
g = 0
for i in a:
    g = gcd(g, i)
ans = set()
ans.add(g % k)
for i in range(k):
    ans.add((i * g) % k)
print(len(ans))
print(*sorted(list(ans)))


