from math import atan2, hypot

def solve():
    N = int(input())
    engines = [tuple(map(int, input().split())) for _ in range(N)]

    engines.sort(key=lambda x: atan2(x[1], x[0]))

    ans = 0
    for L in range(N):
        for R in range(L, L+N):
            x, y = 0, 0
            for i in range(L, R+1):
                i %= N
                dx, dy = engines[i]
                x, y = x+dx, y+dy
            dist = hypot(x, y)
            if dist > ans:
                ans = dist

    print(ans)


solve()

