(n, m, x) = input().split()
list01 = input().split()
list02 = [int(a) for a in list01]
b = sum((c > int(x) for c in list02))
d = sum((e < int(x) for e in list02))
print(min(b, d))
