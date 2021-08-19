t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    o = 0
    for i in a:
        if i % 2 != 0:
            o += 1
    if o == 0:
        print('NO')
    elif o == n and n % 2 == 0:
        print('NO')
    elif o == n and n % 2 == 1:
        print('YES')
    else:
        print('YES')
