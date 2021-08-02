X, Y, Z, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

cakeList = []
for i in range(1, X + 1):
    for j in range(1, Y + 1):
        for k in range(1, Z + 1):
            if i * j * k <= K:
                cakeList.append(A[i - 1] + B[j - 1] + C[k - 1])
            else:
                break

cakeList.sort(reverse=True)

for i in range(K):
    print(cakeList[i])
