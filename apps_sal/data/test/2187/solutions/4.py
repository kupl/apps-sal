T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input().split()]
    print(sum([max(A[i] - A[i + 1], 0) for i in range(N - 1)]))
