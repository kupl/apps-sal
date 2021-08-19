t = int(input())
for _ in range(t):
    (n, k) = list(map(int, input().split()))
    best = 0
    for i in range(2, n + 1):
        if n % i == 0:
            best = i
            break
    print(n + best + 2 * (k - 1))
