import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
a.sort()
if n == 1:
    if a[0] % 2 == 1:
        v = True
    else:
        v = False
else:
    v = True
    c = 0
    for i in range(0, n - 1):
        if a[i] == a[i + 1]:
            c = c + 1
            j = i
    if c > 1:
        v = False
    elif c == 1:
        if a[j] == 0:
            v = False
        if j > 0:
            if a[j - 1] + 1 == a[j]:
                v = False
    if (sum(a) - n * (n - 1) // 2) % 2 == 0:
        v = False
if v == True:
    print('sjfnb')
else:
    print('cslnb')
