n = int(input())
a = list(map(int, input().split()))
if (n == 1 and a != [1]) or (n != 1 and a.count(1) != n - 1):
    print('NO')
else:
    print('YES')

