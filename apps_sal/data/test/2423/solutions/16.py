p=int(input())
a=[]
x=0
for i in range(p-1):
    a+=input().split()
for i in range(p):
    if a.count(str(i+1))==1:
        x+=1
print(x)

