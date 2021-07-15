n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
i = 0
now = 1
all = 0
while i != m:
    if a[i] - now > 0:
        all += a[i] - now
        now = a[i]
    else:
        if a[i] - now < 0:
            all += (n - now) + a[i]
            now = a[i]
 #   print(all, a[i], now)
    i += 1
print(all)
