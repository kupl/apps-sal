n=int(input())
a = [0]*(n+1)
a[0] = [0, 0, 0]
for i in range(n):
    a[i+1]=list(map(int,input().split()))

flag = True
for i in range(n):
    if abs(a[i+1][1]-a[i][1])+abs(a[i+1][2]-a[i][2]) > (a[i+1][0]-a[i][0]):
        flag=False
    elif (abs(a[i+1][1]-a[i][1])+abs(a[i+1][2]-a[i][2])-(a[i+1][0]-a[i][0]))%2==1:
        flag=False

if flag:
    print("Yes")
else:
    print("No")

