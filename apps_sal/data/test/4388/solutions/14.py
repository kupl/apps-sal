n = int(input())
if (n - n % 100) / 100 == 1:
    n += 800
else:
    n -= 800

if (n % 100 - (n % 100) % 10) / 10 == 1:
    n += 80
else:
    n -= 80

if n % 10 == 1:
    n += 8
else:
    n -= 8
print(n)
