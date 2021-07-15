n, k = map(int,input().split())
a = []
for i in range(n+1):
    a.extend(input().split())
if k == 0:
    if a[0] == '0': print('Yes')
    
    elif a[0] == '?' and (n - a.count('?'))% 2 == 0: print('Yes')
    else: print('No')
elif '?' in a:
    if n % 2 == 0: print('No')
    else: print('Yes')
else:
    a = list(map(int, a))[::-1]
    res = a[0]
    for i in range(1, n+1):
        res = a[i] + res * k
        if res > 10**11 or res < -10**11: 
            print('No')
            return
    if res == 0: print('Yes')
    else: print('No')
