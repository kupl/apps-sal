N = int(input())
L = list(map(int, input().split()))
S = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        S += L[i] * L[j]
print(S)
