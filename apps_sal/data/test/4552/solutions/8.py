def dfs(s,N):
    if len(s)==10:
        if "1" in s:
            cal(s,N)
        return
    dfs(s+"0",N)
    dfs(s+"1",N)

def cal(s,N):
    p = 0
    for i in range(N):
        c=0
        for j in range(10):
            c+=F[i][j]*int(s[j])
        p+=P[i][c]
    profit.append(p)
    return

N = int(input())
F=[list(map(int,input().split())) for _ in range(N)]
P=[list(map(int,input().split())) for _ in range(N)]
profit=[]

dfs("",N)
print(max(profit))
