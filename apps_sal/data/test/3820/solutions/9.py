n,m = list(map(int,input().split()))
s = input()
t = input()
x = s.find('*')
if(s==t):
    print('YES')
elif(x==-1):
    print('NO')
elif(n-1>m):
    print('NO')
else:
    if(s[:x]==t[:x]):
        z = s[x+1:]
        z = z[::-1]
        p = t[::-1]
        p = p[:len(z)]
        if(p==z):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

