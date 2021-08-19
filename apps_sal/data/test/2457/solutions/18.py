t = int(input())
for tt in range(t):
    (n, a, b, c, d) = map(int, input().split())
    r1 = a - b
    r2 = a + b
    t1 = c - d
    t2 = c + d
    if r1 * n > t2 or r2 * n < t1:
        print('No')
    else:
        print('Yes')
