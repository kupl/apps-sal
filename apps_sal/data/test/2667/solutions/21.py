n = int(input())

L = [int(x) for x in input().split()]

s = sum(L)

if s == n * (n + 1) // 2:
    print('YES')

else:
    print('NO')
