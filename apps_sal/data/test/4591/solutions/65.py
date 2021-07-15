a,b,c,x,y = map(int, input().split())

# set x >= y
if x < y: 
    x,y = y,x
    a,b = b,a

price_1 = a*x + b*y
price_2 = a*(x-y) + 2*c*y
price_3 = 2*c*x

print(min(price_1, price_2, price_3))
