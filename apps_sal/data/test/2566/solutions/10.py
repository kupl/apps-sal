t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = a.count(1)
    p = n // s
    q = n % s
    if q == 0:
        w = s
    else:
        w = q
    num = float('inf')
    for j in range(7):
        tmp = 0
        cnt = 0
        for k in range(7):
            tmp += a[(j + k) % 7]
            cnt += 1
            if tmp == w:
                num = min(num, cnt)
                break
    if n - s <= 0:
        print(num)
    elif q == 0:
        print(7 * (p - 1) + num)
    else:
        print(7 * p + num)
