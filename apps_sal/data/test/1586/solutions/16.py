n = int(input())
m = n // 10

f = []
while m:
    f.append(m % 5)
    m //= 5

print(0 if n % 2 else sum(a * (5**(i + 1) // 4) for i, a in enumerate(f)))
