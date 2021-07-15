n, k = list(map(int, input().split()))

limit = 4 * 60 - k

for i in range(1, n+1):
    limit -= i * 5
    if limit < 0:
        print(i - 1)
        break
else:
    print(n)

