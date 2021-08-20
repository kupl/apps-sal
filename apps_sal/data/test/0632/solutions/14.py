t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().strip().split()))
    if n % 2 == 0:
        print(n + 2 * k)
    else:
        for i in range(3, n + 1):
            if n % i == 0:
                print(n + i + (k - 1) * 2)
                break
