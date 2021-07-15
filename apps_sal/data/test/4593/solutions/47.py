import math
X = int(input())
beki = []
beki.append(1)
Xruto = math.sqrt(X)
Xruto = math.floor(Xruto)
for i in range(2, Xruto+1):
    for j in range(10):
        a = pow(i, j)
        if a <= X:
            beki.append(a)
        else:
            break
print((max(beki)))

