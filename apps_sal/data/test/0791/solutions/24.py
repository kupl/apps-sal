def solve():
    n=int(input())
    ans=0
    k=input()
    p=1
    if k[0]=='0':
        ans+=1
        print(ans)
    else:
        for i in range(n):
            if p==0:
                break
            else:
                if k[i]=='0':
                    k=k[:i]+'1'+k[i+1:]
                    ans+=1
                    p=0
                else:
                    k=k[:i]+'0'+k[i+1:]
                    ans+=1
        print(ans)
solve()
