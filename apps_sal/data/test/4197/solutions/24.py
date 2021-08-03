N = int(input())
A = list(map(int, input().split()))
B = [0] * N

for n in range(N):
    B[A[n] - 1] = n + 1

print(*B)
