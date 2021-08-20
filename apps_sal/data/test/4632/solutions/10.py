for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    b = [i[1] for i in a]
    if b != sorted(b):
        print('NO')
        continue
    a = [[0, 0]] + a
    s = ''
    for i in range(1, n + 1):
        s += 'R' * (a[i][0] - a[i - 1][0])
        s += 'U' * (a[i][1] - a[i - 1][1])
    print('YES')
    print(s)
