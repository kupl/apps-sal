n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
b.sort()
s = b[-1] + b[-2]
if sum(a) > s:
    print('NO')
else:
    print('YES')
