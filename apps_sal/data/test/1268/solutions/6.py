def read():
    return map(int, input().split())


n = int(input())
a = sum(read())
b = sorted(read())
if b[-1] + b[-2] >= a:
    print('YES')
else:
    print('NO')
