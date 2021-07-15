a,b,c,d = [int(s) for s in input().split()]
prods = [a * c, a * d, b * c, b * d]
print(max(prods))
