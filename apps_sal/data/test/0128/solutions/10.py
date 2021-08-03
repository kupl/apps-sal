n, k = map(int, input().split())
per = n * (n - 1) // 2
if k >= (n // 2):
    print(per)
else:
    print(per - ((n - k * 2 - 1) * (n - k * 2) // 2))
