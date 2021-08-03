from math import factorial
n, m = list(map(int, input().split()))
lights = list(map(int, input().split(' ')))
lights.sort()
lights = [0] + lights
lights.append(n + 1)

x = [lights[i + 1] - lights[i] - 1 for i in range(len(lights) - 1)]
s = sum(x)
prod = factorial(s)
for i in x:
    prod //= factorial(i)

prod %= 10**9 + 7

if len(x) >= 3:
    for i in range(1, len(x) - 1):
        if x[i] > 0:
            prod *= pow(2, x[i] - 1, 10**9 + 7)
print(prod % (10**9 + 7))
