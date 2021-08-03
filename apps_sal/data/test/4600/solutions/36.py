N, M = map(int, input().split())
WA = [0] * N
AC = [0] * N
for i in range(M):
    p, S = map(str, input().split())
    if S == 'WA' and AC[int(p) - 1] != 1:
        WA[int(p) - 1] += 1
    elif S == 'AC':
        AC[int(p) - 1] = 1

Q = 0
for i in range(N):
    if AC[i] > 0:
        Q += WA[i]
print(sum(AC), Q)
