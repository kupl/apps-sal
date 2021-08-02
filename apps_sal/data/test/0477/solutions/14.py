n, m, i, j, a, b = list(map(int, input().split()))


def solve(x, y):
    dx, dy = abs(x - i), abs(y - j)
    if dx % a or dy % b:
        return -1
    elif dx // a % 2 != dy // b % 2:
        return -1
    elif dx == 0 and dy == 0:
        return 0
    elif (i - a < 1 and i + a > n) or (j - b < 1 and j + b > m):
        return -1
    else:
        return max(dx // a, dy // b)


res = -1
for k in ((1, m), (n, 1), (n, m), (1, 1)):
    curr = solve(k[0], k[1])
    if curr != -1 and (res == -1 or curr < res):
        res = curr
print(res if res != -1 else 'Poor Inna and pony!')
