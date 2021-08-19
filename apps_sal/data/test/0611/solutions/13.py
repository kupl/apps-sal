(n, m) = list(map(int, input().split()))
avg = 0
sumd = 0
for i in range(m):
    (x, d) = list(map(int, input().split()))
    avg += x
    if d > 0:
        sumd += d * (n * (n - 1) // 2)
    elif d < 0:
        k = (n - 1) // 2
        sumd += d * k * (k + 1)
        if n % 2 == 0:
            sumd += d * (n // 2)
print(avg + sumd / n)
