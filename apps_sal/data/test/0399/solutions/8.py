rd = lambda:map(int,input().split())
n,m= rd()
if m == 1:
    if n ==0:
        print('Yes')
    else:
        print('No')
else:
    m = m-1
    n = n - m
    print('Yes' if n % 2 ==0 and n>=0 and m>=0 else 'No')
