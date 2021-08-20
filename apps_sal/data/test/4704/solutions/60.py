N = int(input())
A = list(map(int, input().split()))
S = sum(A)
T = [0] * (N + 1)
for i in range(N):
    T[i + 1] = T[i] + A[i]
print(min((abs(S - 2 * T[i]) for i in range(1, N))))
