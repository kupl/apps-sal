n = int(input())

for i in range(1, int(n ** .5) + 1):
    if n % i == 0:
        a = i
print(a, n // a)
