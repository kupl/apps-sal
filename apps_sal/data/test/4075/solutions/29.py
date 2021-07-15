import copy

def dfs(i,lst):
    nonlocal ans
    if i==n:
        ans.append(lst)
        return
    tmp1 = copy.copy(lst)
    tmp1.append(0)
    dfs(i+1,tmp1)
    tmp2 = copy.copy(lst)
    tmp2.append(1)
    dfs(i+1,tmp2)

n,m = map(int,input().split())
ans = []
tmp = [0]
dfs(0,tmp)
#print(ans)
s = []
k = []
for i in range(m):
    tmp = list(map(int,input().split()))
    k.append(tmp[0])
    s.append(tmp[1:])
p = list(map(int,input().split()))
#print(k)
#print(s)
#print(p)
cnt = 0
for i in range(len(ans)):
    cnt_i = 0
    for mi in range(m):
        sum_s = 0
        for ki in range(len(s[mi])):
            sum_s += ans[i][s[mi][ki]]
        if sum_s%2==p[mi]:
            cnt_i += 1
    if cnt_i==m:
        cnt += 1
print(cnt)
