n = int(input())

ab = [list(input().split()) for _ in range(n)]
jpy = 0
btc = 0

for i in range(n):
    if ab[i][1] == "JPY":
        jpy += float(ab[i][0])

    elif ab[i][1] == "BTC":
        btc += float(ab[i][0])

print(jpy + btc * 380000.0)
