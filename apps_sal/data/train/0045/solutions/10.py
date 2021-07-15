l=[]
i=1
while(i<10**18+5):
    l.append((i*(i+1))//2)
    i=i*2+1
t=int(input())
for you in range(t):
    n=int(input())
    count=0
    sum=0
    for i in range(len(l)):
        sum+=l[i]
        if(sum>n):
            break
    print(i)

