t=[]
aa=10
for i in range(5):
    x=int(input())
    y=(x-1)%10
    aa=min(aa,y)
    for i in range(14):
        if 10*i>=x:
            t.append(10*i)
            break
print(sum(t)-10+aa+1)
