t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    oddp = 0
    evenp = 0
    oddq = 0
    evenq = 0
    for i in range(n):
        if p[i] % 2 == 0:
            evenp += 1
        else:
            oddp += 1
    for i in range(m):
        if q[i] % 2 == 0:
            evenq += 1
        else:
            oddq += 1

    print(evenp*evenq + oddp*oddq)

