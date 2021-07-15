
n,k = list(map(int,input().split()))

s =  input()

c = 0

if s[-1]=='#':
    print('NO')
    
else:
    a = 0
    q = 0
    for a in range(n):
        if s[a]=='#':
            q += 1
            if q==k:
                c=1
                break
        else:
            q = 0
            
    if c==0:
        print('YES')
    else:
        print('NO')


