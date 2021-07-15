a,b,k = map(int,input().split())
if a >= k:
    print(str(a - k) + ' ' + str(b))
elif a + b >= k:
    print('0 ' + str(a + b - k))
else:
    print('0 0')
