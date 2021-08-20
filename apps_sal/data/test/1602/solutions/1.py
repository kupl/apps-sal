def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    for j in range(32, -1, -1):
        flg = 0
        for (i, a) in enumerate(A):
            if a >> j & 1:
                flg += 1
                idx = i
                if flg == 2:
                    break
        if flg == 1:
            (A[0], A[idx]) = (A[idx], A[0])
            print(*A)
            return
    print(*A)


def __starting_point():
    main()


__starting_point()
