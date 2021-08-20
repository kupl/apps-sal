for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    k -= 1
    print(k // (n - 1) * n + k % (n - 1) + 1)
