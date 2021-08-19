import math
(n, k) = map(int, input().split())
ans = 0
if n < k:
    for j in range(1, n + 1):
        a = math.ceil(math.log(k / j, 2))
        ans += 1 / n * (1 / 2 ** a)
    print(ans)
else:
    for j in range(1, k):
        a = a = math.ceil(math.log(k / j, 2))
        ans += 1 / n * (1 / 2 ** a)
    ans += (n - k + 1) / n
    print(ans)
