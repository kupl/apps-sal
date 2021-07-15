# cook your dish here
a=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
q=0
for i in range(a):
    if b[i]>=q:
        d.append(i)
        q=c[i]
        
for i in d:
    print(i,end=" ")
