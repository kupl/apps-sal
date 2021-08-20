N = int(input())
A = list(map(int, input().split()))
nom = 1
denom = A[0]
for i in range(1, N):
    nom = nom * A[i] + denom
    denom = denom * A[i]
print(denom / nom)
