q = int(input())
for i in range(q):
    x, y = [int(x) for x in input().split()]
    if x - y == 1:
        print('NO')
    else:
        print('YES')
