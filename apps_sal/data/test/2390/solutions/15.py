def main():
    from collections import namedtuple
    import sys
    input = sys.stdin.readline
    Sushi = namedtuple('Sushi', 'x cal')
    (n, c) = list(map(int, input().split()))
    a = []
    for _ in range(n):
        (x, v) = list(map(int, input().split()))
        a.append(Sushi(x=x, cal=v))
    clock = [0] * (n + 1)
    clock_to_0 = [0] * (n + 1)
    ma = 0
    ma0 = 0
    curr = 0
    for (i, s) in enumerate(a, start=1):
        curr += s.cal
        ma = max(ma, curr - s.x)
        ma0 = max(ma0, curr - s.x * 2)
        clock[i] = ma
        clock_to_0[i] = ma0
    anti = [0] * (n + 1)
    anti_to_0 = [0] * (n + 1)
    ma = 0
    ma0 = 0
    curr = 0
    for (i, s) in zip(list(range(n, -1, -1)), reversed(a)):
        curr += s.cal
        ma = max(ma, curr - (c - s.x))
        ma0 = max(ma0, curr - (c - s.x) * 2)
        anti[i] = ma
        anti_to_0[i] = ma0
    ans = 0
    for exit_pos in range(1, n + 1):
        ans = max(ans, clock_to_0[exit_pos - 1] + anti[exit_pos], anti_to_0[(exit_pos + 1) % (n + 1)] + clock[exit_pos])
    print(ans)


def __starting_point():
    main()


__starting_point()
