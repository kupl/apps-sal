t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))

    summ = 0
    for i in range(n):
        summ += a[i]

    if summ == m:
        print('YES')
    else:
        print('NO')
