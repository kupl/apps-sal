n = int(input())

if n == 2:
    count = 1
else:
    count = 2
divisor = []

d = 2
while d * d < n - 1:
    if (n - 1) % d == 0:
        count += 2
    d += 1
if d * d == n - 1:
    count += 1

d = 2
while d * d < n:
    if n % d == 0:
        divisor.append(d)
        divisor.append(n // d)
    d += 1
if d * d == n:
    divisor.append(d)

for d in divisor:
    tmp = n
    while tmp % d == 0:
        tmp //= d
    if tmp % d == 1:
        count += 1

print(count)
