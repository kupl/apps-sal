n = int(input())
a=[]
b=[]
for i in range(n):
    x,y=map(int, input().split())
    a.append(x)
    b.append(y)

count = 0
for i in range(n-2):
    if (a[i]==b[i] and a[i+1]==b[i+1] and a[i+2]==b[i+2]):
        count += 1
if count!=0:
    print("Yes")
else:
    print("No")
