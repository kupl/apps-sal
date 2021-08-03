n = int(input())
i = 1
while i**2 < n:
    i += 1
if n % i == 0:
    print(i + n // i)
else:
    print(i + n // i + 1)
