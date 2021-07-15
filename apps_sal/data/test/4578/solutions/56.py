nx = list(map(int, input().split()))
n, x = nx[0], nx[1]
ms = [int(input()) for _ in range(n)]
donuts = n
x -= sum(ms)
min_donuts = min(ms)
while x >= min_donuts:
    donuts += 1
    x -= min_donuts

print(donuts)

