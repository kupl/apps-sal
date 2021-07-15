


a,b,c,x,y = list(map(int,input().split()))

price = a * x + b * y


for i in range(max(x,y) + 1):
    ab = 2 * i
    cand = ab * c + a * max(0, x - i) + b * max(0, y-i)

    price = min(price, cand)

print(price)
  

