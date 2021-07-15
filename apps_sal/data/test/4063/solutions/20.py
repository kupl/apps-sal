N = int(input())
P = int(N/2)
A = list(map(int, input().split()))
A.sort()

S = A[P] - A[P-1]

print(S)

