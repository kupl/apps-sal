a = [list(map(int,input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for i in range(n)]
visited = [[False for i in range(3)] for j in range(3)]
for i in b:
    for j in range(3):
        for k in range(3):
            if i==a[j][k]:
                visited[j][k] = True

ans = "No"
for i in visited:
    if i==[True,True,True]:
        ans = "Yes"

for i in range(3):
    flag = True
    for j in range(3):
        if visited[j][i]==False:
            flag = False
            break
    if flag:
        ans = "Yes"

if visited[0][0] and visited[1][1] and visited[2][2]:
    ans = "Yes"
if visited[2][0] and visited[1][1] and visited[0][2]:
    ans = "Yes"
print(ans)
