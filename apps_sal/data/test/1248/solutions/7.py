d1, d2, d3 = map(int, input().split(" "))
res = min(d1+d2+d3, min(2*d2+2*d3, min(2*d1+2*d3, 2*d1+2*d2)))
print(res)
