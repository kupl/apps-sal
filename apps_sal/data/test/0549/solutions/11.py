n = int(input())

i = 1

r = 1, n

while i * i <= n:
    if n % i == 0:
        r = i, n // i
    i += 1

print(r[0], r[1])
