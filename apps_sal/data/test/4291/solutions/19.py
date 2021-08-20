(N, Q) = map(int, input().split())
S = list(input())
lsline = []
for i in range(Q):
    lsline.append(list(map(int, input().split())))
lsAC = [0, 0]
AC = 0
for i in range(N - 1):
    if S[i] == 'A' and S[i + 1] == 'C':
        AC += 1
    lsAC.append(AC)
for i in range(Q):
    print(lsAC[lsline[i][1]] - lsAC[lsline[i][0]])
