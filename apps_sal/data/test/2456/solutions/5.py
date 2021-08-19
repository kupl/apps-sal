t = int(input())
for _ in range(t):
    (n, r) = list(map(int, input().split()))
    if r < n:
        print(r * (r + 1) // 2)
    else:
        print(n * (n - 1) // 2 + 1)
