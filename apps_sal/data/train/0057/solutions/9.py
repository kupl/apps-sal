T = int(input())
for i in range(T):
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[-1] > a[0]:
        print('YES')
    else:
        print('NO')
