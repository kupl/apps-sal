import sys
3
n = int(sys.stdin.readline())
b = [int(x) for x in sys.stdin.readline().split()]
b.sort()
if b[0] == b[-1]:
    print(0, n * (n - 1) // 2)
else:
    d = b[-1] - b[0]
    i = 0
    while b[i] == b[i + 1]:
        i += 1
    j = n - 1
    while b[j] == b[j - 1]:
        j -= 1
    print(d, (i + 1) * (n - j))
