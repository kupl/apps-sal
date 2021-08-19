from math import ceil
(n, k) = map(int, input().split())
ans = 0
for x in range(2, 2 * n + 1):
    cd = x - k
    if cd < 2 or cd > 2 * n:
        continue
    p = min(x - 1, 2 * n - x + 1)
    q = min(cd - 1, 2 * n - cd + 1)
    ans = ans + p * q
print(ans)
