from sys import stdin
n = int(stdin.readline().strip())
s = list(map(int, stdin.readline().strip().split()))
en = [0 for i in range(10**6 + 7)]
vis = [0 for i in range(10**6 + 7)]
ans = [0]
flag = True
cnt = 0
v = []
for i in range(n):
    ans[-1] += 1
    vis
    if s[i] > 0:
        en[s[i]] += 1
        vis[s[i]] += 1
        v.append(s[i])
        cnt += 1
    else:
        en[-s[i]] -= 1
        cnt -= 1
    s[i] = abs(s[i])
    if en[s[i]] < 0 or en[s[i]] > 1 or vis[s[i]] > 1:
        flag = False
        break

    if i > 0 and cnt == 0:
        ans.append(0)
        for j in v:
            vis[j] = 0
        v = []

if flag == False or ans[-1] != 0:
    print(-1)
else:
    if ans[-1] == 0:
        ans.pop()
    print(len(ans))
    print(*ans)
