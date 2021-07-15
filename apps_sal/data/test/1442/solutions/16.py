n, s = list(map(int, input().split()))
buy = {}
sale = {}
for i in range(n):
    cur = input().split()
    p = int(cur[1])
    q = int(cur[2])
    if cur[0] == 'B':
        if p in buy:
            buy[p] += q
        else:
            buy[p] = q
    else:
        if p in sale:
            sale[p] += q
        else:
            sale[p] = q

items = list(sale.items())
items.sort()
items = items[:s]
items.reverse()
for i in items:
    print('S', i[0], i[1])
    
items = list(buy.items())
items.sort()
items.reverse()
c = 0
for i in items:
    if c == s:
        break
    print('B', i[0], i[1])
    c += 1

