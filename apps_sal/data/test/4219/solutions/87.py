N = int(input())
xy = [[] for _ in range(N)]

for i in range(N):
    A = int(input())
    for _ in range(A):
        xy[i].append(list(map(int, input().split())))
lst = [[0 for j in range(N)] for k in range(2**N)]

for l in range(2**N):
    for m in range(N):
        if (l >> m) & 1:
            lst[l][m] = 1

ans = 0
for n in lst:
    flag = True
    for f in range(N):
        if n[f] == 1:
            for g in xy[f]:
                if n[g[0] - 1] != g[1]:
                    flag = False
                    break
        else:
            tmp = 0
            for g in xy[f]:
                if n[g[0] - 1] == g[1]:
                    tmp += 1
            if tmp == len(n):
                flag = False
        if not flag:
            break
    if flag:
        ans = max(ans, n.count(1))
print(ans)
