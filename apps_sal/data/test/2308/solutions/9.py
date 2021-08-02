import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x = input().strip()
    y = input().strip()
    m = len(x)
    n = len(y)
    c = 1
    while True:
        if y[n - c] == '1':
            break
        else:
            c += 1
    j = m - c
    k = 0
    while (j >= 0):
        if x[j] == '1':
            print(k)
            break
        else:
            j -= 1
            k += 1
