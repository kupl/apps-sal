n = int(input())
a = 0
for i in reversed(range(1, int(n**(1 / 2)) + 1)):
    if n % i == 0:
        a = i
        break
b = int(n / a)
print(a + b - 2)
