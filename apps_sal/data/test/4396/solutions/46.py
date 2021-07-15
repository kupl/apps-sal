N = int(input())
j = 0
for i in range(N):
    x,u = map(str,input().split())
    x = float(x)
    if u == 'BTC':
        j += x*380000
    if u == 'JPY':
        j += x
print(j)
