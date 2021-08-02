t = int(input())
for i in range(t):
    n, a, b, c, d = list(map(int, input().split()))
    minall = c - d
    maxall = c + d
    minone = a - b
    maxone = a + b
    if minone * n > maxall or maxone * n < minall:
        print('No')
    else:
        print('Yes')
