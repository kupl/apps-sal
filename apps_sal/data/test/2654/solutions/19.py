def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        (a, b) = list(map(int, input().split()))
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N & 1:
        j = (N - 1) // 2
        ans = B[j] - A[j] + 1
        print(ans)
        return
    j = N // 2 - 1
    k = N // 2
    ans = B[j] + B[k] - (A[j] + A[k]) + 1
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
