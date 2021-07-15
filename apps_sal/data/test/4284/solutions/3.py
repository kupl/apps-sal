for i in range(int(input())):
    k, n, a, b = list(map(int, input().split()))
    if k <= n * b:
        print(-1)
        continue
    if (k - n * b) % (a - b) == 0:
        print(min((k - n * b) // (a - b) - 1, n))
    else:
        print(min(int((k - n * b) / (a - b)), n))

