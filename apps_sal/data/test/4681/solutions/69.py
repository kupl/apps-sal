
N = int(input())
L = [2, 1] + [0] * (N - 1)
for i in range(2, N + 1):
    L[i] = L[i - 1] + L[i - 2]

print(L[N])
