for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if k == 1:
        print(n)
    else:
        ans = 0
        while n != 0:
            if n % k == 0:
                n //= k
                ans += 1
            else:
                q = n - n // k * k
                ans += q
                n = n // k * k
        print(ans)

