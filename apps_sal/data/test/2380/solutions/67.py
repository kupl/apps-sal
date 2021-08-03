import collections


def main():
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    bc = [list(map(int, input().split())) for _ in range(m)]
    A.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i, j = 0, 0

    while i < n and j < m:
        if A[i] >= bc[j][1]:
            break
        A[i] = bc[j][1]
        i += 1
        bc[j][0] -= 1
        if bc[j][0] == 0:
            j += 1
    print((sum(A)))


def __starting_point():
    main()


__starting_point()
