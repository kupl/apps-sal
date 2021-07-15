n,m = list(map(int,input().split(" ")))
g = []
good = []
for i in range(n):
    g.append(input().split(" "))
    for j in range(m):
        if g[i][j] == "1":
            good.append((i,j))

c = 4

for i in good:
    if i[0] == 0 or i[1] == 0 or i[0] == n-1 or i[1] == m-1:
        c = 2
        
print(c)

