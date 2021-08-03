ar = [(pow(2, x) - 1) * pow(2, x - 1) for x in range(1, 100)]
n = int(input())
mx = 1
for x in ar:
    if n % x == 0:
        mx = x
print(mx)
