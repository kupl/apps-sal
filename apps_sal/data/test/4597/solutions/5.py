N = int(input())
p = 1
for n in range(1, N + 1):
    p = p * n % (pow(10, 9) + 7)
print(p)
