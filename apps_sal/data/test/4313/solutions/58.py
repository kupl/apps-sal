N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
D = []
a = 0
for i in range(len(C)):
    D.append(V[i] - C[i])
for i in range(len(D)):
    if D[i] >= 1:
        a += D[i]
print(a)
