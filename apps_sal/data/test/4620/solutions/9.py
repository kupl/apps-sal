N = int(input())
C = []
S = []
F = []
for _ in range(N-1):
    c, s, f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

for i in range(N):
    t = 0
    for j in range(i, N-1):
        if t < S[j]:
            t = S[j]
        elif t % F[j] != 0:
            t += F[j]-t%F[j]
        t += C[j]
    print(t)
