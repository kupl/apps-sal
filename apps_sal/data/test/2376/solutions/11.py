(N, W) = map(int, input().split())
(W1, V1) = map(int, input().split())
P = {W1: [V1], W1 + 1: [], W1 + 2: [], W1 + 3: []}
for i in range(1, N):
    (w, v) = map(int, input().split())
    P[w].append(v)
PS = {}
for (k, v) in P.items():
    v.sort(reverse=True)
    S = [0] * (len(v) + 1)
    for i in range(len(v)):
        S[i + 1] = S[i] + v[i]
    PS[k] = S
(A, B, C, D) = (len(PS[W1]), len(PS[W1 + 1]), len(PS[W1 + 2]), len(PS[W1 + 3]))
ans = 0
for a in range(A):
    for b in range(B):
        for c in range(C):
            for d in range(D):
                if a * W1 + b * (W1 + 1) + c * (W1 + 2) + d * (W1 + 3) > W:
                    continue
                ans = max(ans, PS[W1][a] + PS[W1 + 1][b] + PS[W1 + 2][c] + PS[W1 + 3][d])
print(ans)
