t = int(input())
for ii in range(t):
    n, k = map(int, input().split())
    if n % 2 == 0:
        print(n + 2 * k)
    else:
        f = 0
        for j in range(2, n + 1):
            if n % j == 0:
                print(n + j + 2 * (k - 1))
                break
