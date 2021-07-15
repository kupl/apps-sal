a,b,c,d = [int(s) for s in input().split()]
prods = [a * c, a * d, b * c, b * d]
m = max(prods)
print(m)
