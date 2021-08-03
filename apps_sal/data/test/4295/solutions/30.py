x, y = map(int, input().split())

z = x % y
p = y - z
if(z < p):
    print(z)
else:
    print(p)
