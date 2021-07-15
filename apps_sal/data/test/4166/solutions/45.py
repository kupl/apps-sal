n, m = map(int, input().split())
ans = [-1] * n
exist = True
for i in range(m):
    s, c = map(int, input().split())
    if (n != 1 and (s, c) == (1, 0)) or (ans[s - 1] != -1 and ans[s - 1] != c):
        exist = False
        break
    else:
        ans[s - 1] = c

if exist:
    for i in range(n):
        if n != 1 and i == 0:
            if ans[i] == -1:
                ans[i] = 1
        else:
            if ans[i] == -1:
                ans[i] = 0
    print(*ans, sep='')
else:
    print(-1)
