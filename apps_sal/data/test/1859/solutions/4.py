n = int(input())
i = 2
m = 0
while n % i != 0 and i * i <= n:
    i += 1
if n % i == 0:
    m += 1
    n -= i
    m += n // 2
    print(m)
else:
    print(1)
