t = int(input())
for i in range(t):
    n = int(input())
    data = tuple(map(int, input().split()))
    f = data[0] % 2
    for i in data:
        if i % 2 != f:
            print('NO')
            break
    else:
        print('YES')
