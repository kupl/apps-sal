n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
b.sort()
if b[-1] + b[-2] >= sum(a):
    print('YES')
else:
    print('NO')
