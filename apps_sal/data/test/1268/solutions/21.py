n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = sorted(b)
if b[-1] + b[-2] >= sum(a):
    print('YES')
else:
    print('NO')
