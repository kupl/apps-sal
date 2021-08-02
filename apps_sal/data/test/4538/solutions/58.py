n, d = list(map(int, input("").split()))
o = 0
for i in range(n):
    x, y = list(map(int, input("").split()))
    if x**2 + y**2 <= d**2:
        o += 1
print(o)
