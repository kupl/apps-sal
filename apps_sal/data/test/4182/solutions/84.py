n,m,x,y=list(map(int, input().split()))
x_list=[int(i) for i in input().split()]
y_list=[int(i) for i in input().split()]

ans="War"

for i in range(x+1, y+1):
    if max(x_list)<i<=min(y_list):
        ans="No War"
        break

print(ans)

