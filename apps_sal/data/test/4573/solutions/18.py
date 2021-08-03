N = int(input())
X = list(map(int, input().split()))
x = sorted(X)
ms = x[N // 2 - 1]
for i in range(N):
    if X[i] > ms:
        print(ms)
    else:
        print(x[N // 2])
