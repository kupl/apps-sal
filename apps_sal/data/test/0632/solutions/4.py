q = int(input())
for _ in range(q):
    (n, k) = list(map(int, input().split()))
    if n % 2:
        for d in range(3, n + 1):
            if n % d == 0:
                n += d
                k -= 1
                break
    n += k * 2
    print(n)
