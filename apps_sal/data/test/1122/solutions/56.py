n, m = list(map(int, input().split()))
if n % 2 == 1:
    for i in range(m):
        print((n - i - 1, i + 1))
else:
    cnt = 1
    for i in range(m):
        if i % 2 == 0:
            print((n // 4 - i // 2, n // 4 - i // 2 + cnt))
        else:
            print((n // 2 + n // 4 - i // 2, n // 2 + n // 4 - i // 2 + cnt))
        cnt += 1
