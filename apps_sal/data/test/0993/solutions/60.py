from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
ssum = [0] * (n + 1)
for i in range(n):
    ssum[i + 1] = (ssum[i] + a[i]) % m
c = Counter(ssum)
ans = 0
for v in c.values():
    ans += v * (v - 1) // 2
print(ans)
