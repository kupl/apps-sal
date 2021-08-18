X, N = map(int, input().split())
if N == 0:
    P = []
else:
    P = list(map(int, input().split()))
    P = sorted(P)
assert len(P) == N
cands = []
x = X
while True:
    if x not in P:
        cands.append(x)
        break
    x -= 1
x = X
while True:
    if x not in P:
        cands.append(x)
        break
    x += 1
a, b = cands
if abs(a - X) > abs(b - X):
    print(b)
else:
    print(a)
