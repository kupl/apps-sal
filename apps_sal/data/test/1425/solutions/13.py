import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
a.sort(reverse=True)
if a[0] >= a[1] + a[2]:
    print('NO')
else:
    b = [a[2 * i] for i in range(0, (n + 1) // 2)]
    c = [a[2 * i + 1] for i in range(0, n // 2)]
    c.reverse()
    print('YES')
    x = b + c
    print(' '.join(list(map(str, x))))
