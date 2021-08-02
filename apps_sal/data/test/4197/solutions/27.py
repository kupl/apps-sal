N = int(input())
A = tuple(map(int, input().split()))
L = [0] * N
for i in range(N):
    L[A[i] - 1] = i + 1
print(*L)
