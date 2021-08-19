a = int(input())
for i in range(a):
    (x, y) = list(map(int, input().split()))
    z = list(map(int, input().split()))
    if sum(z) == y:
        print('YES')
    else:
        print('NO')
