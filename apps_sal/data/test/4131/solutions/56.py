n,m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
b = [[] for _ in range(n+1)]
for i in range(m):
    b[a[i][0]].append((a[i][1],i+1))
#print(b)
for i in range(1,n+1):
    b[i].sort()
ans = ["."]*m
for i in range(1,n+1):
    for j in range(len(b[i])):
        ans[b[i][j][1]-1] = "0"*(6-len(str(i))) + str(i) + "0"*(6-len(str(j+1))) + str(j+1)
print(*ans, sep="\n")
