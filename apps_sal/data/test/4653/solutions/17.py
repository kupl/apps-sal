for nt in range(int(input())):
    (n, k) = map(int, input().split())
    a = n % k
    if a > k // 2:
        print(n - (a - k // 2))
    else:
        print(n)
