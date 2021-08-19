A = list(map(int, input().split()))
K = int(input())
A.sort()
A[2] = A[2] * 2 ** K
print(sum(A))
