n = int(input())
a = [int(ai) for ai in input().split()]
if len(a) == 1 and a[0] == 1 or (len(list((ai for ai in a if ai == 0))) == 1 and len(a) > 1):
    print('YES')
else:
    print('NO')
