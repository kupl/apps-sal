N, M = list(map(int, input().split()))
S, C = [], []
for _ in range(M):
    s, c = list(map(int, input().split()))
    S.append(s - 1)
    C.append(c)

if M != 0 and N != 1 and S[0] == 0 and C[0] == 0:
    print((-1))
    return

d = {}
for s, c in zip(S, C):
    if c != d.setdefault(s, c):
        print('-1')
        return

ans = ""
for i in range(N):
    if i in d:
        ans += str(d[i])
    else:
        ans += "0"

if ans[0] == "0" and N != 1:
    ans = '1' + ans[1:]
print(ans)

