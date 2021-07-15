f=int(input())
a=sum(list(map(int,input().split())))
r=[1]
for i in range(f):
    r.append(0)
p=5
j=(a%(f+1))-1
for i in range(j,j+5):
    if r[(i+1)%(f+1)]==1:
        p-=1
print(p)
