for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    ans = n // k * k + min(k // 2, n % k)
    print(ans)
