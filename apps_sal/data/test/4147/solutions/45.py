n,A,B,C=map(int,input().split())
Q=[int(input()) for ii in range(n)]
inf=10**15
def dfs(now,a,b,c):
    if now==n:
        return abs(a-A)+abs(b-B)+abs(c-C) if 0 not in [a,b,c] else inf
    q1= dfs(now+1,a,b,c)
    q2= dfs(now+1, a+Q[now],b,c)+10
    q3= dfs(now+1, a, b+Q[now], c)+10
    q4 = dfs(now+1,a,b,c+Q[now])+10
    return min(q1,q2,q3,q4)
 
print(dfs(0,0,0,0)-30)
