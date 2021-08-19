t = int(input())
for _ in range(t):
    (n, m, x, y) = [int(x) for x in input().split()]
    mp = [input() for _ in range(n)]
    if y >= 2 * x:
        print(x * sum((sum((1 for x in row if x == '.')) for row in mp)))
    else:
        tot = 0
        for row in mp:
            i = 0
            while i < m:
                if i + 1 < m and row[i] == row[i + 1] == '.':
                    tot += y
                    i += 2
                elif row[i] == '.':
                    tot += x
                    i += 1
                else:
                    i += 1
        print(tot)
