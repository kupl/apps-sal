import sys
sys.setrecursionlimit(10 ** 8)


def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]


def main():
    H, W = ZZ()
    A = [ZZ() for _ in range(H)]
    done = [[False] * W for _ in range(H)]
    path = []
    operation = []

    for i in range(H):
        if i % 2:
            for j in range(W)[::-1]:
                path.append([i, j])
        else:
            for j in range(W):
                path.append([i, j])
    for i in range(H * W - 1):
        x, y = path[i]
        nx, ny = path[i + 1]
        if A[x][y] % 2:
            operation.append([x, y, nx, ny])
            A[x][y] -= 1
            A[nx][ny] += 1

    print((len(operation)))
    for i, j, k, l in operation:
        print((i + 1, j + 1, k + 1, l + 1))

    return


def __starting_point():
    main()


__starting_point()
