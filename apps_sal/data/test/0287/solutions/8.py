n, k = list(map(int, input().split()))
low = -1
high = -1
if k == 0:
    low = 0
    high = 0
else:
    if k == n:
        low = 0
        high = 0
    else:
        low = 1
        if n >= 3 * k:
            high = 2 * k
        else:
            high = n - k
print(low, high)
