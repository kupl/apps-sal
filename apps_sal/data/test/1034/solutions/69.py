
X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

ABC = []
for x in range(X):
    for y in range(Y):
        for z in range(Z):
            if (x + 1) * (y + 1) * (z + 1) <= K:
                ABC.append(A[x] + B[y] + C[z])
            else:
                break

ABC.sort(reverse=True)
for i in range(K):
    print(ABC[i])
