N = int(input())

A = [[] for _ in range(2)]
for i in range(2):
    A[i] = list(map(int, input().split()))

AmeMax = 0
for n in range(1, N + 1):
    preAme = sum(A[0][:n]) + sum(A[1][n - 1:])
    if AmeMax < preAme:
        AmeMax = preAme

print(AmeMax)
