n, k = list(map(int, input().split()))
i = 1
while True:
    if n % (k - i) == 0:
        print(n // (k - i) * k + k - i)
        break
    i += 1
