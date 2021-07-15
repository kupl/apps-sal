def main():
    n = int(input())
    red = []
    red_used = [[False for _ in range(2 * n)] for _ in range(2 * n)]
    for _ in range(n):
        rp = list(map(int, input().split()))
        red.append(rp)
        red_used[rp[0]][rp[1]] = True
    ans = 0
    red.sort(key=lambda x: x[1], reverse=True)
    blue = [list(map(int, input().split())) for _ in range(n)]
    blue.sort(key=lambda x: x[0])
    for bx, by in blue:
        for rx, ry in red:
            if rx < bx and ry < by and red_used[rx][ry]:
                red_used[rx][ry] = False
                ans += 1
                break
    print(ans)


def __starting_point():
    main()

__starting_point()
