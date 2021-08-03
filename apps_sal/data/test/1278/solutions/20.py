import sys
n, x, y = list(map(int, input().split()))
*a, = list(map(int, input().split()))

for i in range(n):
    for j in range(max(0, i - x), i):
        if a[j] <= a[i]:
            break
    else:
        for k in range(i + 1, min(i + y + 1, n)):
            if a[k] <= a[i]:
                break
        else:
            print(i + 1)
            return
