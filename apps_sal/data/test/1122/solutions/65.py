(n, k) = list(map(int, input().split()))
if n % 2 == 1:
    p = 1
    q = n
    for i in range(k):
        print(f'{p} {q}')
        p += 1
        q -= 1
else:
    p = 1
    q = n
    for i in range(k):
        print(f'{p} {q}')
        if abs(p - q) == n // 2 + 1:
            p += 1
        p += 1
        q -= 1
        if abs(p - q) == n // 2:
            p += 1
