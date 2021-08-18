N, A, B = map(int, input().split())
if A * B < N or A + B > N + 1:
    print(-1)
    return
X = [[i * B] for i in range(A)]
s = N - A
i = 0
while s:
    if len(X[i]) >= B:
        i += 1
    X[i].append(X[i][-1] - 1)
    s -= 1
Y = []
for x in X:
    for xx in x:
        Y.append(xx)

D = {a: i for i, a in enumerate(sorted(Y))}
Y = [D[y] + 1 for y in Y]
print(*Y)
