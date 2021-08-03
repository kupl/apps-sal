import sys
input = sys.stdin.readline


def solve(n, points):
    ans = []
    x, y = 0, 0
    for i in range(n):
        xi, yi = points[i]
        if xi < x or yi < y:
            print('NO')
            return
        ans += ['R'] * (xi - x) + ['U'] * (yi - y)
        x, y = xi, yi
    print('YES')
    print(''.join(ans))


for _ in range(int(input())):
    n = int(input())
    points = [list(map(int, input().split())) for i in range(n)]
    points.sort()
    solve(n, points)
