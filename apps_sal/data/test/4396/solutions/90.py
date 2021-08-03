N = int(input())
l = [0] * N

for i in range(N):
    x, y = map(str, input().split())
    l[i] = float(x)
    if y == "BTC":
        l[i] *= 380000.0

ans = sum(l)
print(ans)
