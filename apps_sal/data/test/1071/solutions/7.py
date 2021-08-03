a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
n = int(input())
if (a - 1) // 5 + 1 + (b - 1) // 10 + 1 > n:
    print('NO')
else:
    print('YES')
