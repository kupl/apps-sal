(X, Y, A, B, C) = list(map(int, input().split()))
P = list([[int(s), 1] for s in input().split()])
Q = list([[int(s), 2] for s in input().split()])
R = list([[int(s), 0] for s in input().split()])
L = P + Q + R
L.sort(reverse=True, key=lambda x: x[0])
T = X + Y
(nr, ng, total) = (0, 0, 0)
ans = 0
for i in range(A + B + C):
    (a, l) = L[i]
    if l == 1 and nr < X:
        nr += 1
        ans += a
        total += 1
    if l == 2 and ng < Y:
        ng += 1
        ans += a
        total += 1
    if l == 0:
        ans += a
        total += 1
    if total == T:
        break
print(ans)
