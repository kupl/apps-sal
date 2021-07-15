n = int(input())
jpy = 0
btc = 0
rate = 380000
for _ in range(n):
    x, y = input().split()
    if y == "JPY":
        jpy += int(x)
    else:
        btc += float(x)
print((jpy + btc * rate))

