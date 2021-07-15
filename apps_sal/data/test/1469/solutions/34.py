L = t = int(input())
X = []
B = 4
while L:
    X.append(L%B)
    L//=B

E = []
N = len(X)*2
for i, x in enumerate(X[:-1]):
    r = B**i
    t -= r*x
    for k in range(0, x):
        E.append((2*i+1, 2*i+2, r*k))

    E.append((2*i+2, 2*i+3, 0))

    for k in range(x, B):
        E.append((2*i+1, 2*i+3, r*k))

    E.append((2*i+2, N, t))

for k in range(0, X[-1]):
    E.append((N-1, N, B**(len(X)-1)*k))

print(N, len(E))
for e in E:
    print(*e)
