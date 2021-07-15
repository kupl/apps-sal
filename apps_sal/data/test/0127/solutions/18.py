n , f = list(map(int,input().split()))
total_products = 0
sale_list = []
for i in range(n):
    p , c = list(map(int,input().split()))
    total_products += min(p,c)
    sale_list.append((min(2*p,c),min(p,c)))

sale_list.sort(key = lambda x:x[0]-x[1])
for i in range(f):
    add = sale_list.pop()
    total_products = total_products + add[0] - add[1]

print(total_products)
