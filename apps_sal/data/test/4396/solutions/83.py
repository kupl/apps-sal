n = int(input())
c = 0
for i in range(n):
    y, t = input().split()
    if t == 'BTC':
        yen = float(y) * 380000.0
    else:
        yen = float(y)
    c += yen

print(c)
