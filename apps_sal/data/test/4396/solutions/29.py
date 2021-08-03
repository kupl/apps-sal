n = int(input())
c = 0
for i in range(n):
    x, u = input().split()
    if u == "BTC":
        c += float(x) * 380000
    else:
        c += int(x)
print(c)
