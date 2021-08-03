def solve():
    N = int(input())

    A = [int(k) for k in input().split()]

    res = 0

    for i in range(1, N - 1):
        if A[i] == 0 and A[i - 1] == A[i + 1] == 1:
            A[i + 1] = 0
            res += 1

    print(res)


solve()
