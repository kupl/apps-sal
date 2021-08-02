import sys
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)

ans = 0
mod = 10**9 + 7
b = sorted(list(cnt.keys()), reverse=True)
m = cnt[b[0]]

for key in b[1:]:
    m += cnt[key]
    ans = (ans + pow(m, mod - 2, mod) * key * cnt[key]) % mod

for i in range(2, n + 1):
    ans = ans * i % mod

print(ans)
