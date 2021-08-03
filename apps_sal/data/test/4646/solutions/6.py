t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    badEven = 0
    badOdd = 0
    for i in range(n):
        if i % 2 != a[i] % 2 and i % 2 == 0:
            badEven += 1
        elif i % 2 != a[i] % 2 and i % 2 == 1:
            badOdd += 1
    if badEven == badOdd:
        print(badEven)
    else:
        print(-1)
