books,reads=list(map(int,input().split()))

booksw=list(map(int,input().split()))

readl=list(map(int,input().split()))

res=[]

for b in readl:
    if(b not  in res):
        res.append(b)
sum=0
for l in readl:
    for b in res:
        if(b==l):
            res.remove(b)
            poped=b
            break
        sum=sum+booksw[b-1]
    res=[poped]+res

print(sum)

