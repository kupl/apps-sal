n = int(input())
A = list(map(int, input().split()))

A = list(set(A))

if len(A) == n:
    print('YES')
else:
    print('NO')
