n, k = map(int, input().split())
if n % (2 * k + 1) == 0 or n % (2 * k + 1) >= k + 1:
    if n % (2 * k + 1) == 0:
        print(n // (2 * k + 1))
    else:
        print(n // (2 * k + 1) + 1)
    j = k + 1
    while j <= n:
        print(j, end=' ')
        j += 2 * k + 1
else:
    print(n // (2 * k + 1) + 1)
    j = 1
    while j <= n:
        print(j, end=' ')
        j += 2 * k + 1
