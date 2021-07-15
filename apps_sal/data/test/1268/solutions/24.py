n = int(input())
cans = []
cola = [int(x) for x in input().split()]
cans = sorted([int(x) for x in input().split()])
c = sum(cola)
if c <= cans[-1] + cans[-2]:
    print('YES')
else:
    print('NO')
