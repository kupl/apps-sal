import sys


def main():
    input = sys.stdin.readline
    (A, B) = list(map(int, input().split()))
    (h, w) = (100, 100)
    G = [[0] * w for _ in range(h)]
    for i in range(50):
        for j in range(w):
            G[i][j] = 1
    (A, B) = (A - 1, B - 1)
    for i in range(0, 50, 2):
        if A <= 0:
            break
        for j in range(0, 100, 2):
            if A <= 0:
                break
            G[i][j] = 0
            A -= 1
    for i in range(99, 50, -2):
        if B <= 0:
            break
        for j in range(0, 100, 2):
            if B <= 0:
                break
            G[i][j] = 1
            B -= 1
    print((h, w))
    for i in range(h):
        print(''.join(['.' if G[i][j] == 0 else '#' for j in range(w)]))


def __starting_point():
    main()


__starting_point()
