n = int(input())
A = list(map(int, input().split()))
add = sum(A)
req = n * (n + 1) // 2
if add == req:
    print('YES')
else:
    print('NO')
