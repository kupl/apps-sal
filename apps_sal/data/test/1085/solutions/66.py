import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    N = int(input())
    P = []
    for k in range(1, 1 + int((N - 1) ** (1 / 2))):
        if (N - 1) % k == 0:
            P.append((N - 1) // k)
            P.append(k)
    P = set(P)
    ans = len(P)
    for k in range(2, 1 + int(N ** (1 / 2))):
        if N % k == 0:
            t = N // k
            while t % k == 0:
                t //= k
            if t % k == 1:
                ans += 1
    print(ans)


def __starting_point():
    main()


__starting_point()
