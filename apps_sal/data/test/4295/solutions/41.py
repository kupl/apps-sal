N, K = list(map(int, input().split()))
P = N % K
A = [P, K - P]

if A[0] <= A[1]:
    print((A[0]))
elif A[0] > A[1]:
    print((A[1]))
