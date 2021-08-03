mod = 1000000007
n = int(input())
cat = [0] * 1100
f, c, i = 1, 1, 1
while i < 1100:
    cat[i] = f
    i += 1
    c = c * (8 * i - 12) // i
    f = c - f
cat = cat[1:-1]
sm = 0
for i in range(3, n + 3):
    sm += (cat[i - 1] + (-1) ** (i - 1)) // (1 << i)
print(sm % mod)
