F = []


def gen(T, X):
    if len(X) == 5:
        F.append(list(X))
        return
    for item in T:
        H = list(T)
        H.remove(item)
        X.append(item)
        gen(H, X)
        X.remove(item)
    return


G = []
for i in range(5):
    G.append(list(map(int, input().split())))
gen([0, 1, 2, 3, 4], [])
ans = 0
for item in F:
    X = item
    t = 0
    for i in range(5):
        for j in range(i, 5, 2):
            if j == 4:
                continue
            t += G[X[j]][X[j + 1]]
            t += G[X[j + 1]][X[j]]
    ans = max(ans, t)
print(ans)
