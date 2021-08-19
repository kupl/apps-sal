import math
(n, k) = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    a = max(math.ceil(math.log2(k / i)), 0)
    ans += 0.5 ** a
print(ans / n)
