def main():
    import sys

    def input():
        return sys.stdin.readline().strip()
    N = int(input())
    CSF = [list(map(int, input().split())) for _ in range(N - 1)]
    for i in range(N):
        t = 0
        for (c, s, f) in CSF[i:]:
            if t <= s:
                t = s
            else:
                t = ((t - s) // f if (t - s) % f == 0 else (t - s) // f + 1) * f + s
            t += c
        print(t)


def __starting_point():
    main()


__starting_point()
