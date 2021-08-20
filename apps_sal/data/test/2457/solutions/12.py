t = int(input())
for _ in range(t):
    (n, a, b, c, d) = list(map(int, input().split()))
    mg = n * (a - b)
    Mg = n * (a + b)
    mp = c - d
    Mp = c + d
    if mg <= Mp and Mg >= mp:
        print('Yes')
    else:
        print('No')
