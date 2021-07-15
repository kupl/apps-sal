n = int(input())
btc = 380000.0
a = 0
# 単位毎に加算する。
for _ in range(n):
    x, u = input().split()
    if u == 'JPY':
        a += int(x)
    elif u == 'BTC':
        a += float(x)*btc
print(a)

