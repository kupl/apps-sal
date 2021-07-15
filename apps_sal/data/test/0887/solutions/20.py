n=int(input())
s=input().split()
t=False
if n==1:
    if s[0]=='0':
        print('NO')
        return
    else:
        print('YES')
        return
else:
    for i in range(n):
        if s[i]=='0':
            if t:
                print('NO')
                return
            else:
                t=True
if not t:
    print('NO')
else:
    print('YES')

