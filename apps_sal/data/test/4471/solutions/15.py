t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    s = set()

    for i in heights:
        s.add(i % 2)

        if len(s) == 2:
            break

    if len(s) == 1:
        print('YES')
    else:
        print('NO')
