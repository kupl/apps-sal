n = int(input())
a = list(map(int, input().split()))
b= sorted(list(map(int, input().split())))
if sum(a) <= b[-1] + b[-2]:
    print('YES')
else:
    print('NO')
