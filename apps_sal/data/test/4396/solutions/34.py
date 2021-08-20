n = int(input())
y = 0
for i in range(n):
    (x, u) = input().split()
    if u == 'JPY':
        y += int(x)
    if u == 'BTC':
        y += 100000 * float(x) / 100000 * 380000.0
print(y)
