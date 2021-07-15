n=int(input())
pro=[int(i) for i in input().split()]
book={}
for i in pro:
    if i in book:
        book[i]+=1
    else:
        book[i]=1
book=[book[i] for i in book]
book=sorted(book,reverse=True)
book.insert(0,0)
ans=0
l=len(book)
for i in range(1,book[1]+1):
    pos,cur,tem=2,i,i
    while cur&1 == 0 and pos <l:
        cur>>=1
        if book[pos]<cur :
            break
        tem+=cur
        pos+=1
    ans=max(ans,tem)
print(ans)
