(N, M) = map(int, input().split())
s = [0] * (M + 1)
c = [0] * (M + 1)
for i in range(1, M + 1):
    (s[i], c[i]) = map(int, input().split())
ans = ['*'] * N
flag = 0
for i in range(1, M + 1):
    if ans[s[i] - 1] == '*' or ans[s[i] - 1] == c[i]:
        ans[s[i] - 1] = c[i]
    else:
        flag = 1
if ans[0] == '*' and len(ans) >= 2:
    ans[0] = 1
ans = list(map(lambda x: 0 if x == '*' else x, ans))
if flag == 1 or all((x == 0 for x in ans)) or ans[0] == 0:
    if len(ans) == 1 and ans[0] == 0:
        print(ans[0])
    else:
        print(-1)
else:
    ans = ''.join(map(str, ans))
    print(ans)
