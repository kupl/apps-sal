n = int(input())
P = list(map(int, input().split()))
K = 0
for i in range(n - 2):
    if P[i] < P[i + 1] and P[i + 1] < P[i + 2] or (P[i + 2] < P[i + 1] and P[i + 1] < P[i]):
        K += 1
print(K)
