for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    pos = sorted([int(x) - 1 for x in input().split()]) + [10 ** 9]
    ans = sorted(a)
    l = pos[0]
    for i in range(m):
        if pos[i] + 1 < pos[i + 1]:
            a[l:pos[i] + 2] = sorted(a[l:pos[i] + 2])
            l = pos[i + 1]
    if a == ans:
        print('YES')
    else:
        print('NO')
