def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 1
    A.sort()
    if N % 2 == 0:
        for i in range(0, N, 2):
            if A[i] != A[i + 1] or A[i] != i + 1:
                print(0)
                return
            ans = ans * 2 % mod
        print(ans)
    else:
        if A[0] != 0:
            print(0)
            return
        ans = 1
        for i in range(1, N, 2):
            if A[i] != A[i + 1] or A[i] != i + 1:
                print(0)
                return
            ans = ans * 2 % mod
        print(ans)


def __starting_point():
    main()


__starting_point()
