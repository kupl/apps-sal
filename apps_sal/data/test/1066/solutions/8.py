n, k = map(int, input().split())
if k <= int((n + n % 2) / 2):
    print(2 * (k - 1) + 1)
else:
    tmp = k - int(n / 2) - n % 2
    print(2 * tmp)
