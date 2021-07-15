n=int(input())
rez=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if(b-a)>=2:
        rez+=1
print(rez)

