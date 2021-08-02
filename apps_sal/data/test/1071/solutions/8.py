b = sum(list(map(int, input().split())))
a = sum(list(map(int, input().split())))
n = int(input())
if (a + 9) // 10 + (b + 4) // 5 <= n:
    print('YES')
else:
    print('NO')
