n = int(input())
for i in range(n):
    (a, b) = [int(i) for i in input().split()]
    if a == b == 2 or a == 1 or b == 1:
        print('YES')
    else:
        print('NO')
