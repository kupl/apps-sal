def solve(n, a):
    if n <= 2:
        return 0
    d = [v - u for (u, v) in zip(a, a[1:])]
    max_d = max(d)
    min_d = min(d)
    if max_d - min_d > 4:
        return -1
    min_cnt = -1
    for d in range(min_d, max_d + 1):
        for d0 in range(-1, 2):
            y = a[0] + d0
            valid = True
            cnt = 0 if d0 == 0 else 1
            for x in a[1:]:
                dx = abs(y + d - x)
                if dx > 1:
                    valid = False
                    break
                cnt += dx
                y += d
            if valid:
                if cnt < min_cnt or min_cnt < 0:
                    min_cnt = cnt
    return min_cnt


def main():
    n = int(input())
    a = [int(_) for _ in input().split()]
    ans = solve(n, a)
    print(ans)


def __starting_point():
    main()


__starting_point()
