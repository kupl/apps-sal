f=int(input())
a=sum(list(map(int,input().split())))
p=5
j=(a%(f+1))-1
for i in range(j,j+5):
    if (i+1)%(f+1)==0:
        p-=1
print(p)
