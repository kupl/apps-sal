n = int(input())
a = [int(x) for x in input().split()]
b = sorted([int(x) for x in input().split()])
if sum(a) <= b[-1] + b[-2]:
    print('YES')
else:
    print('NO')

