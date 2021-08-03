n = int(input())
jpy = btc = 0
for i in range(n):
    x, u = map(str, input().split())
    if u == "JPY":
        jpy += int(x)
    else:
        btc += float(x)

ans = jpy + 380000.0 * btc
print(ans)
