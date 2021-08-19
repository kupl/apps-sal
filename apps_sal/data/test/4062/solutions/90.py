(a, b, c, d) = (int(x) for x in input().split())
list = [a * c, a * d, b * c, b * d]
print(max(list))
