n = int(input()) 
base = list(map(int, input().split())) 
stock = [0 for k in range(int(1e6+1))]
for zbi in base : 
    stock[zbi] = 1 
t = base[-1] 
for k in range(2,n+1) : 
    num = base[n-k]
    for i in range(2, (t//num)+1) : 
        if stock[i*num] >= 1  : 
            stock[num] = max(stock[num], 1 + stock[i*num] )
print(max(stock))
