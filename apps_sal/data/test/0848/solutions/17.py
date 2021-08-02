n, k = map(int, input().split())
if(n * k > (n * (n - 1) // 2)):
    print(-1)
else:
    print(n * k)
    for i in range(n):
        for j in range(1, k + 1):
            print(i + 1, ((i + j) % n) + 1)
