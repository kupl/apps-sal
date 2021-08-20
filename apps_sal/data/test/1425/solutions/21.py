n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[-2] + a[-3] <= a[-1]:
    print('NO')
else:
    print('YES')
    print(' '.join(map(str, a[:-2] + [a[-1], a[-2]])))
