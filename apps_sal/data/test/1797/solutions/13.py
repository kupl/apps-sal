n = int(input())
p = list(map(int, input().split(" ")))
ls = []
vis = [False for i in range(n)]
cnt = 0
for i in range(n):
    j = i
    cnt = 0
    while not(vis[j]):
        vis[j] = True
        cnt += 1
        j = p[j] - 1
    if cnt>0:
        ls.append(cnt)
ls.sort()
if len(ls)>1:
    ls[-2] += ls[-1]
    ls.pop()
ans=0
for i in ls:
    ans=ans+i**2
print(ans)

