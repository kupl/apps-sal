N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

F = [0] * len(S)
for i in range(N - 1):
    F[i + 1] += F[i] + (1 if S[i:i + 2] == 'AC' else 0)
for l, r in LR:
    print(F[r - 1] - F[l - 1])
