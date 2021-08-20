n = int(input())
a = list(map(int, input().split()))
s = sum(a)
if n == 1:
    print('NO')
elif s % 200 == 0:
    if s // 200 == n and n % 2 == 1:
        print('NO')
    else:
        print('YES')
else:
    print('NO')
