n = int(input())
a = sorted(list(map(int, input().split())))[::-1]
if(a[0] < a[1] + a[2]):
    print('YES')
    print(a[0], *a[2:], a[1])
else:
    print('NO')
