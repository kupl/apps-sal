for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    i = 1
    ans = n
    while i * i <= n:
        if n % i == 0:
            if i <= k:
                ans = min(ans, n // i)
            if n // i <= k:
                ans = min(ans, i)
        i += 1
    print(ans)
