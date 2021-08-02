

def main():
    N, T = map(int, input().split())
    l = []
    for _ in range(N):
        c, t = map(int, input().split())
        l.append((c, t))
    l.sort()
    for e in l:
        if e[1] <= T:
            print(e[0])
            return
    print("TLE")


def __starting_point():
    main()


__starting_point()
