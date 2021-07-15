s=input()
def rr(a): #圧縮された要素を保持
    ll,l=[],1
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            l+=1
        else:
            ll.append([l,a[i]])
            l=1
    ll.append([l,a[-1]])
    return ll
ss=rr(s)
ans=[0]*len(s)
count=0
for i in range(0,len(ss),2):
    r,l=ss[i][0],ss[i+1][0]
    count+=r
    ans[count]+=r//2+(l+1)//2
    ans[count-1]+=(r+1)//2+l//2
    count+=l
print(*ans)
