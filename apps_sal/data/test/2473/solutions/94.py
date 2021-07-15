N, K = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]
x_sort = sorted(XY, key=lambda x: x[0])


def check(l, r, b, t):
    cnt = 0
    for x, y in XY:
        if r >= x and x >= l and t >= y and b >= y:
            cnt += 1
    return cnt >= K


ans = 10**20

for i in range(N - K + 1):
    xl = x_sort[i][0]
    for j in range(i + K - 1, N):
        dx = x_sort[j][0] - xl

        points = sorted(x_sort[i: j+1], key=lambda x: x[1])

        rest = j - i + 1
        for p in range(rest - K + 1):
            yd = points[p][1]
            for q in range(p + K - 1, rest):
                dy = points[q][1] - yd
                ans = min(ans, dx*dy)

print(ans)

