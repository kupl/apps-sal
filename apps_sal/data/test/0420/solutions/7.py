(n, m) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


def pol(x, y):
    if y % 2 != 0:
        return False
    (l, r) = (0, y - 1)
    while l < r:
        if a[l][x] != a[r][x]:
            return False
        l += 1
        r -= 1
    return True


result = 1
for i in range(m):
    j = n
    while pol(i, j):
        j //= 2
    result = max(result, j)
print(result)
