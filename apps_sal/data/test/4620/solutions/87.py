N = int(input())
C = [0] * (N-1)
S = [0] * (N-1)
F = [0] * (N-1)
for i in range(N-1):
    C[i], S[i], F[i] = map(int,input().split())

for i in range(N):
    t = 0
    for j in range(i,N - 1):
        if t < S[j]:
            t = S[j]
        elif t % F[j] == 0:
            pass
        else:
            t = t + F[j] - (t % F[j])
        t += C[j]
    print(t)
