n, m = list(map(int, (input().split())))
xSum = 0
res = 0
posMult = n * (n - 1) // 2;
negMult = n // 2 * (1 + n // 2)
if (n % 2 == 0):
    negMult -= n // 2

for i in range(m):
    x, d = list(map(int, (input().split())))
    xSum += x
    if d < 0:
        res += negMult * d
    else:
        res += posMult * d

print(xSum + res/n)

