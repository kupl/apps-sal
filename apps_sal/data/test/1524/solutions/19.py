S = str(input())
N = len(S)
con = []
border = []
for i in range(N - 1):
    if S[i] == 'L' and S[i + 1] == 'R':
        border.append(i)
    elif S[i] == 'R' and S[i + 1] == 'L':
        con.append(i)
border.append(N - 1)
ans = [0] * N
now = -1
for i in range(len(con)):
    pp = border[i] - now
    if pp % 2 == 0:
        ans[con[i]] += pp / 2
        ans[con[i] + 1] += pp / 2
    elif (con[i] - now) % 2 == 0:
        ans[con[i]] += (pp - 1) / 2
        ans[con[i] + 1] += (pp + 1) / 2
    else:
        ans[con[i]] += (pp + 1) / 2
        ans[con[i] + 1] += (pp - 1) / 2
    now = border[i]
for i in range(N):
    print(int(ans[i]), end=' ')
