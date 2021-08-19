(K, X) = map(int, input().split())
L = str()
for i in range(-K + 1, K):
    L += str(X + i) + ' '
print(L)
