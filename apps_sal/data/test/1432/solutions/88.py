def main():
    import sys
    def input(): return sys.stdin.readline().strip()

    N = int(input())
    A = list(map(int, input().split()))

    tmp = 0
    for i in range(N):
        if i % 2 == 0:
            tmp += A[i]
        else:
            tmp -= A[i]

    ans = [tmp]
    for i in range(N - 1):
        tmp = (A[i] - tmp // 2) * 2
        ans.append(tmp)

    print(*ans)


def __starting_point():
    main()


__starting_point()
