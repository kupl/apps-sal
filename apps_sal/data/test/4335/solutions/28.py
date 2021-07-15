b=int(input())
a=input()
c=[]
for i in range(b):
    c.append(a[i])
#a = list(map(int,input().split()))
#b = list(map(int,input().split()))

if b==1:
    print("No")
elif c[:int(b/2)]==c[int(b/2):]:
    print("Yes")
else:
    print("No")

