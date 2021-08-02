n = int(input())
c = 0

d = [100, 20, 10, 5, 1]

for i in d:
    c += n // i
    n = n % i

print(c)
