(a, b, c, d) = (int(x) for x in input().split())
aa = []
aa.append(a * c)
aa.append(a * d)
aa.append(b * c)
aa.append(b * d)
print(max(aa))
