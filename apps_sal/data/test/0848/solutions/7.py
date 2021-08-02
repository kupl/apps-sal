n, k = list(map(int, input().split(" ")))
if 2 * k + 1 > n:
    print(-1)
else:
    print(n * k)
    for i in range(1, n + 1):
        for j in range(0, k):
            print(i, (i + j) % n + 1)
