n,m,k = list(map(int,input().split()))
l = []
for i in range(n+2):
    l.append([0 for i in range(m+2)])
ans = 0
done = 'no'
for i in range(k):
    x,y = list(map(int,input().split()))
    l[x][y] = 1
    if done == 'no' and ((l[x][y-1] == 1 and l[x-1][y] == 1 and l[x-1][y-1] == 1) or (l[x][y-1] == 1 and l[x+1][y] == 1 and l[x+1][y-1] == 1) or (l[x-1][y] == 1 and l[x][y+1] == 1 and l[x-1][y+1] == 1) or (l[x+1][y+1] == 1 and l[x+1][y] == 1 and l[x][y+1] == 1)):
        ans = i+1
        done = 'yes'
print(ans)

