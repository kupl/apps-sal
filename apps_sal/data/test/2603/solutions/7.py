import sys
T = int(sys.stdin.readline().strip())
for t in range(0, T):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    m = min(a)
    b = sorted(a)
    v = True
    for i in range(0, n):
        if a[i] != b[i] and a[i] % m != 0:
            v = False
    if v == True:
        print('YES')
    else:
        print('NO')
