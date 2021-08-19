import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
mod = 998244353
n = int(input())
cnt = [0] * (10 ** 6 + 1)
kids = []
for i in range(n):
    (k, *a) = map(int, input().split())
    for ai in a:
        cnt[ai] += 1
    kids.append(a)
inv_n = pow(n, mod - 2, mod)
ans = 0
for i in range(n):
    k = len(kids[i])
    for ai in kids[i]:
        ans += inv_n * pow(k, mod - 2, mod) * inv_n * cnt[ai]
        ans %= mod
print(ans)
