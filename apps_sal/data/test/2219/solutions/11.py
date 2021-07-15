t = int(input())
for i in range(0, t):
    n, k = map(int, input().split())
    c = 0
    while (n != 0):
        if (n % k != 0):
            c += n%k
            n = n - n%k
        else:
            c += 1
            n = n // k
    print(c)
