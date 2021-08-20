import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7


def main():
    n = int(input())
    ans = [[0 for _ in range(n)] for _ in range(n)]
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    u = list(map(int, input().split()))
    v = list(map(int, input().split()))
    for i in range(n):
        if not s[i]:
            for j in range(n):
                ans[i][j] = ans[i][j] | u[i]
        if not t[i]:
            for j in range(n):
                ans[j][i] = ans[j][i] | v[i]
    for i in range(n):
        for j in range(n):
            if u[i] & v[j]:
                ans[i][j] = ans[i][j] | u[i] & v[j]
    for x in range(n):
        if not s[x]:
            continue
        x_sum = ans[x][0]
        for y in range(n):
            x_sum = x_sum | ans[x][y]
        if x_sum == u[x]:
            continue
        up = u[x] - x_sum
        for y in range(n):
            if t[y]:
                continue
            y_mul = ans[0][y]
            for i in range(n):
                if i == x:
                    continue
                y_mul = y_mul & ans[i][y]
            up_y = ~y_mul & up
            ans[x][y] += up_y
            up -= up_y
            if not up:
                break
    for y in range(n):
        if not t[y]:
            continue
        y_sum = ans[0][y]
        for x in range(n):
            y_sum = y_sum | ans[x][y]
        if y_sum == v[y]:
            continue
        up = v[y] - y_sum
        for x in range(n):
            if s[x]:
                continue
            x_mul = ans[x][0]
            for j in range(n):
                if y == j:
                    continue
                x_mul = x_mul & ans[x][j]
            up_x = ~x_mul & up
            ans[x][y] += up_x
            up -= up_x
            if not up:
                break
    for i in range(n):
        check_xs = ans[i][0]
        check_ys = ans[0][i]
        check_xm = ans[i][0]
        check_ym = ans[0][i]
        for j in range(n):
            check_xs = check_xs | ans[i][j]
            check_ys = check_ys | ans[j][i]
            check_xm = check_xm & ans[i][j]
            check_ym = check_ym & ans[j][i]
        if s[i] and u[i] != check_xs:
            print(-1)
            return
        if t[i] and v[i] != check_ys:
            print(-1)
            return
        if not s[i] and u[i] != check_xm:
            print(-1)
            return
        if not t[i] and v[i] != check_ym:
            print(-1)
            return
    for i in range(n):
        print(*ans[i])


def __starting_point():
    main()


__starting_point()
