n, k = map(int, input().split())
X = []
for i in range(n):
    t, d = map(int, input().split())
    X.append([t, d])

X.sort(key=lambda x: x[1], reverse=True)

V = set()
point = 0
S = []

for t, d in X[:k]:
    point += d
    if t in V:
        S.append(d)
    else:
        V.add(t)
point += len(V)**2

ans = point

for t, d in X[k:]:
    if not S:
        break
    if not t in V:
        point += d - S.pop() + 1 + len(V) * 2
        V.add(t)
        ans = max(ans, point)

print(ans)
