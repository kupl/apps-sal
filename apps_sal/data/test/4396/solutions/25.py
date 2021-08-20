n = int(input())
jpy = 0
btc = 0
for i in range(n):
    (a, b) = input().split()
    if b == 'JPY':
        jpy += int(a)
    else:
        btc += int(float(a) * 100000000)
print(jpy + btc * 38 / 10000)
