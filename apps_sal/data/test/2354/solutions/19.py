import sys
n, k = list(map(int, sys.stdin.readline().split()))
half = n // 2
add = 0
res = 0
y = 0
x = 0
for i in range(k):
    y, x = list(map(int, sys.stdin.readline().split()))
    if n % 2 == 0:
        add = 0
        if (y + x) % 2 != 0:
            add = n * n // 2
        res = add + half * (y - 1) + (x + 1) // 2
    else:
        if y % 2 == x % 2:
            res = ((n * (y - 1) + 1) // 2) + (x + 1) // 2
        else:
            res = ((n * n + 1) // 2) + ((n * (y - 1) + 1) // 2) + (x + 1) // 2
            if y % 2 == 0:
                res -= 1
    print(res)
