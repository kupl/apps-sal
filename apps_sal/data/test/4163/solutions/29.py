n=int(input())
a=[list(map(int,input().split())) for i in range(n)]
x=0
y=0
for i in range(n):
    if a[i][0]==a[i][1]:
        x+=1
    else:
        x=0
    if x==3:
        print("Yes")
        y+=1
        break
if y==0:
    print("No")
