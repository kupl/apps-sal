N,A,B,C = map(int,input().split())
l = [int(input()) for n in range(N)]
inf = 10 ** 18

def dfs(cur,a,b,c):
    if cur == N:
        if min(a,b,c) > 0:
            return abs(A-a)+abs(B-b)+abs(C-c)-30
        else:
            return inf

    res0 = dfs(cur+1,a,b,c)
    res1 = dfs(cur+1,a+l[cur],b,c)+10
    res2 = dfs(cur+1,a,b+l[cur],c)+10
    res3 = dfs(cur+1,a,b,c+l[cur])+10
    return min(res0,res1,res2,res3)
print(dfs(0,0,0,0))
