a = list(map(int,input().split()))
A = a[0]
B = a[1]

if (A+B) % 2 == 0:
    print(((A+B)//2))
else:
    print('IMPOSSIBLE')

