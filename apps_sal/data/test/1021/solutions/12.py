n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
y=[]
for i in range(1,n):
    x.append(a[i]-a[i-1])
for i in range(1,n):
    y.append(b[i]-b[i-1])
x.sort()
y.sort()
if x==y and a[0]==b[0] and a[-1]==b[-1]:
    print("Yes")
else:
    print("No")
