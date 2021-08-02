b = sum(map(int, input().split()))
a = sum(map(int, input().split()))
n = int(input())
if a // 10 + b // 5 + (1 if a % 10 != 0 else 0) + (1 if b % 5 != 0 else 0) <= n:
    print('YES')
else:
    print('NO')
