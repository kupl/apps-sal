t = int(input())
for _ in range(t):
    (n, m) = list(map(int, input().split()))
    ar = [['B'] * m for i in range(n)]
    ar[0][0] = 'W'
    for x in ar:
        s = ''
        for y in x:
            s += y
        print(s)
