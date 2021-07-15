n,m = (int(i) for i in input().split())
q = set(map(int,input().split()))
s = 0
k = 1
ansv = 0
ans = []
while s < m:
    
    if not k in q:
        if s+k <=m:
            s+=k
            ans+=[k]
            ansv+=1
        else:
            break
    k+=1
    
    
print(ansv)
print(' '.join(list(map(str,ans))))

