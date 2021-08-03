n, k = list(map(int, input().split()))
if(k > (n - 1) // 2):
    print(-1)
else:
    print(n * k)
    for i in range(1, n + 1):
        for j in range(k):
            print(i, (i + j) % n + 1)
