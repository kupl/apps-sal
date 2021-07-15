a = int(input())
digits = sorted(map(int, list(input())))
b = sum(digits)
n = 0
while b < a:
    b += 9 - digits[n]
    n += 1
print(n)
