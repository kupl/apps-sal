n = int(input())
sm = 0
for i in range(n):
    x, u = input().split()
    x = float(x)
    if u == "BTC":
        x *= 380000.0
    sm += x
print(sm)
