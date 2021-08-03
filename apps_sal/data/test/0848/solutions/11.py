n, k = list(map(int, input().split(" ")))
if (n % 2 == 0 and k > n // 2 - 1) or (n % 2 == 1 and k > n // 2):
    print(-1)
else:
    print(n * k)
    for i in range(n):
        for j in range(k):
            if i + j + 2 > n:
                print(i + 1, i + j + 2 - n)
            else:
                print(i + 1, i + j + 2)
