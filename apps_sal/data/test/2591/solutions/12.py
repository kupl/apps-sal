t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    if n % 2 == 0:
        (l, r) = (n // 2 - 1, n // 2)
    else:
        print(a[n // 2], end=' ')
        (l, r) = (n // 2 - 1, n // 2 + 1)
    while l > -1 and r < n:
        print(a[l], a[r], end=' ')
        l -= 1
        r += 1
    print()
