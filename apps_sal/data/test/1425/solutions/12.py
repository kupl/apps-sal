n = int(input())
a = sorted([int(x) for x in input().split()])
if a[-1] < a[-2] + a[-3]:
    print('YES')
    print(*(a[-2:-1] + a[-1:] + a[-3:-2] + a[:-3]))
else:
    print('NO')
