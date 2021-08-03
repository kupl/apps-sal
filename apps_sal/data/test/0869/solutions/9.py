a, b = input().split()
a = int(a)
b = int(b)

m = min(a, b)


x = max(a, b)

r = (x - m) // 2

print(m, r)
