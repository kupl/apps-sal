n, m=map(int,input().split())
A=[input() for _ in range(n)]
B=[input() for _ in range(m)]

def dfs(y, x):
    for Y in range(m):
        for X in range(m):
            if A[y+Y][x+X]!=B[Y][X]:
                return False
    return True

ans="No"
for y in range(n-m+1):
    for x in range(n-m+1):
        if A[y][x]==B[0][0]:
            if dfs(y,x):
                ans="Yes"
                break
    else:
        continue
    break

print(ans)
