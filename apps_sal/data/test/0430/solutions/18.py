count = int(input())
apples = input().split()
sto = apples.count('100')
dv = apples.count('200')

if sto % 2 == 1 or (dv % 2 == 1 and sto < 2):
    print('NO')
else:
    print('YES')

