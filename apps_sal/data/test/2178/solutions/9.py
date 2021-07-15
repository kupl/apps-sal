n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=a[::-1]
c=[0]*n
bk=[]
for i in range(n):
    co=0
    if c[b[i]-1]==0:
        while a[-1]!=b[i]:
            co+=1
            c[a[-1]-1]=1
            a.pop()
        co+=1
        c[a[-1]-1]=1
        a.pop()
    bk.append(co)
print(*bk)
                

