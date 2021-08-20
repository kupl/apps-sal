t = int(input())
for _ in range(t):
    (n, a, b, c, d) = list(map(int, input().split()))
    mn = (a - b) * n
    mx = (a + b) * n
    mic = c - d
    max = c + d
    if mic > mx or max < mn:
        print('No')
    else:
        print('Yes')
