A,B = map(int,input().split())

if A%2 != B%2:
    print('IMPOSSIBLE')
else:
    print(int(abs(A+B)/2))
