n, k = map(int, input().split())
if k % 2 == 0:
    print(int(n / k)**3 + (int((n - k / 2) / k + 1)**3))
else:
    print(int(n / k)**3)
