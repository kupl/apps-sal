a,b,c = list(map(int, input().split()))
if c > a:
    c-=a
    if c != 1:
        
        c %= b
        if c == 0 or c==1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
elif c==a:
    print('YES')
else:
    print('NO')
