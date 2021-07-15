a=int(input())
b,c=map(int,input().split())
s=[]
total=a+c
for i in range(a):
    s.append(int(input()))
for i in s:
    for j in range(2,b+1):
        if i==1:
            total+=1
        elif j%i==1:
            total+=1
print(total)
