N = int(input())

jpy = 0
btc = 0

for _ in range(N):
    x, u = input().split()
    if u == "JPY":
        jpy += int(x)
    else:
        btc += float(x)

print(jpy + btc * 380000)
