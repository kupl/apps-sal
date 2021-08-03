from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = (s[i - 1] + a[i - 1]) % m
c = Counter(s)
ans = 0
for k, v in c.items():
    if k == 0:
        ans += v - 1 + (v - 2) * (v - 1) // 2
    else:
        ans += v * (v - 1) // 2
print(ans)
