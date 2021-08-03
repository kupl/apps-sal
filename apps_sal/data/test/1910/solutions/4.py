n = int(input())
tot = 2 * n - 2
ans = 0
for i in range(tot - n + 1):
    p = 4
    l = 1 + i
    if l > 1:
        p = p * 3
    for j in range(100):
        if 1 + j < l - 1:
            p = p * 4
    if l + n - 1 < tot:
        p = p * 3
    for j in range(100):
        if tot - j > l + n:
            p = p * 4
    ans = ans + p
print(ans)
