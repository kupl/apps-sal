#!python3

def LI(): return list(map(int, input().split()))


# input
N = int(input())
UV = [LI() for _ in range(N - 1)]


def main():
    ans = N * (N + 1) * (N + 2) // 6
    for u, v in UV:
        if u > v:
            u, v = v, u
        ans -= u * (N - v + 1)
    print(ans)


def __starting_point():
    main()


__starting_point()
