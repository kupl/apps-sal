n, k = map(int, input().split())

ans = 0

for i in range(2, 2 * n + 1):

    if i > n:
        ab = 2 * n - i + 1
    else:
        ab = i - 1

    r = i - k
    if r <= 1 or r >= 2 * n + 1:
        cd = 0
    elif r > n:
        cd = 2 * n - r + 1
    else:
        cd = r - 1

    ans += ab * cd

print(ans)
