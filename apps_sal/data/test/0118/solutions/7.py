t, s, x = [int(x) for x in input().split()]
x -= t
if x>=0 and (x%s == 0 or ((x-1)%s == 0 and x != 1)):
    print('YES')
else:
    print('NO')
    

