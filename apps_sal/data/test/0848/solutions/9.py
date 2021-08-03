n, k = input().split()
n = int(n)
k = int(k)
if(n < 2 * k + 1):
    print(-1)

else:
    print(n * k)
    for i in range(1, n + 1):
        for j in range(k):
            print(i, (i + j) % n + 1)
