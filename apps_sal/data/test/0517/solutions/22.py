# Codeforces 639B #

n, d, h = list(map(int, input().split()))

if h < ((d + 1) >> 1) or (n > 2 and d == 1):
    
    print(-1)
    
else:
    k = 2 if h != 1 else 1
    print(h + 1, k)
    for i in range(2, h):
        print(i, i + 1)
    if h != 1: print(h, 1)
    if h < d: print(1, h + 2)
    for i in range(h + 2, d + 1):
        print(i, i + 1)
    for i in range(d + 2, n + 1):
        print(i, k)

