
#k=int(input())
#n,m=map(int,input().split())

#a=list(map(int,input().split()))

#b=list(map(int,input().split()))


n=int(input())
a=set(map(int,input().split()))


cnt=0
for i in a:
    if i>0:
        cnt+=1

print(cnt)
