def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(N - 1):
        A[i + 1] = (A[i + 1] + A[i]) / 2
    print(A[-1])
    return


solve()
