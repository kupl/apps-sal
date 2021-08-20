(N, M) = map(int, input().split())
p_S = [input().split() for _ in range(M)]
AC = [False] * N
WA = [0] * N
for i in range(M):
    num = int(p_S[i][0]) - 1
    if AC[num] == 0 and p_S[i][1] == 'WA':
        WA[num] += 1
    elif AC[num] == 0 and p_S[i][1] == 'AC':
        AC[num] = True
    else:
        continue
s = 0
for i in range(N):
    if AC[i]:
        s += WA[i]
print(sum(AC), s)
