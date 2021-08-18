def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(1, N + 1):
        A[i - 1] -= i
    A.sort()
    b = A[N // 2]
    ans = 0
    for a in A:
        ans += abs(a - b)
    print(ans)


def __starting_point():
    main()


__starting_point()
