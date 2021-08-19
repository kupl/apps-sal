from sys import stdin, stdout
from decimal import Decimal
(n, k) = map(int, stdin.readline().split())
values = list(map(Decimal, stdin.readline().split()))
cnt = [values[0]]
for i in range(1, n):
    cnt.append(cnt[-1] + values[i])
cnt.append(0)
ans = 0
for i in range(k - 1, n):
    ans += cnt[i] - cnt[i - k]
stdout.write(str(ans / Decimal(n - k + 1)))
