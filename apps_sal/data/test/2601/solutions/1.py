t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if all((x > y for (x, y) in zip(a, a[1:]))):
        print('NO')
    else:
        print('YES')
