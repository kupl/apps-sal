from sys import stdin
tt = 1
for loop in range(tt):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    maxans = 0
    for i in range(3):
        maxans += min(a[i], b[(i + 1) % 3])
    b = [b[1], b[2], b[0]]
    minans = 0
    for i in range(3):
        now = a[i]
        for j in range(3):
            if i != j:
                now -= b[j]
        minans = max(minans, now)
    for i in range(3):
        now = b[i]
        for j in range(3):
            if i != j:
                now -= a[j]
        minans = max(minans, now)
    print(minans, maxans)
