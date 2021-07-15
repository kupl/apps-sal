n,k=list(map(int,input().split(' ')))
s=input()
setl=set(s)
l=sorted(list(setl))
cnt=0
if k>n:
    print(s+(k-n)*l[0])
else:
    ans=""
    for j in range(k-1,-1,-1):
        cnt+=1
        if s[j]==l[-1]:
            ans+=l[0]
        else:
            x=l.index(s[j])
            ans+=l[x+1]
            break
    print(s[0:k-cnt]+ans[::-1])
        

