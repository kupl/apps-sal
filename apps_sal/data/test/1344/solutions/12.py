N = int(input())
A = [int(i) for i in input().split()]
L = [1 for _ in range(N)]
for i in range(1, N):
    if A[i] > A[i - 1]:
        L[i] = 1 + L[i - 1]
print(max(L))
