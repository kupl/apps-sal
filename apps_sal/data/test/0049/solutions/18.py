index = int(input())

total = 9
n = 1

while index > total:
    total += (n + 1) * (10**n) * 9
    n += 1
last = 10**(n - 1)
total -= n * 9 * last
index = index - total


r = index % (n)
k = index // n

number = last + k


if r == 0:
    print(str(number - 1)[n - 1])
else:
    print(str(number)[r - 1])
