n, k = list(map(int, input().split()))
m = 10000000000000000000
for i in range(1, k):
    if n % i == 0:
        x = i + (k * (n // i))
        if m > x:
            m = x
print(m)

