a=[]
for i in range(4):
    a.append([int(i) for i in input().split()])
for i in range(4):
    if a[i][3]==1:
        if any([a[i][0],a[i][1],a[i][2],a[(i+1)%4][0],a[(i+2)%4][1],a[(i+3)%4][2]]):
            print("YES")
            break
else:
    print("NO")

