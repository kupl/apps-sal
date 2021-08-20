(N, M) = map(int, input().split())
S = []
C = []
ans = []
for i in range(M):
    (s, c) = map(int, input().split())
    S.append(s)
    C.append(c)
for i in range(10 ** (N + 1)):
    Str = str(i)
    if len(Str) == N and all([Str[S[j] - 1] == str(C[j]) for j in range(M)]):
        ans.append(i)
if ans == []:
    print(-1)
else:
    print(min(ans))
