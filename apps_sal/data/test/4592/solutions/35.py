import math
n = int(input())
mod = 10**9 + 7
ans = 1
cnt = [0] * 1000
for i in range(2, n + 1):
    x = i
    for j in range(2, int(math.sqrt(n)) + 1):
        while x % j == 0:
            cnt[j] += 1
            x /= j
    if x != 1:
        cnt[int(x)] += 1
for i in cnt:
    if i != 0:
        ans *= (i + 1)
        ans %= mod
print(int(ans))
