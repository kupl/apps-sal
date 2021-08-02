n = int(input())
while any(n % i == 0 for i in range(2, int(n**.5) + 1)):
    n += 1
print(n)
