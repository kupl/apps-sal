from collections import defaultdict
n, m, aim = list(map(int, input().split()))

g = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(n):
    ls = [int(i) for i in input().split()]
    for j in range(m):
        g[i + 1][j + 1] = ls[j]

ans = 0
dp = defaultdict(int)

def search(x, y, is_l, mk):
    if x < 1 or y < 1 or x > n or y > m:
        return

    if is_l:
        mk ^= g[x][y]
        if x + y - 1 == n:
            dp[(x, y, mk)] += 1
        else:
            search(x + 1, y, is_l, mk)
            search(x, y + 1, is_l, mk)
    else:
        if abs(x - n) + abs(y - m) + 1 == m:
            # print(x, y, mk)
            nonlocal ans
            ans += dp[(x, y, mk)]
        else:
            mk ^= g[x][y]
            search(x - 1, y, is_l, mk)
            search(x, y - 1, is_l, mk)

search(1, 1, True, 0)
search(n, m, False, aim)

print(ans)

