def input_as_list():
    return list(map(int, input().split()))


x, y, z = input_as_list()
n = (x + y) // z

xr, yr = x % z, y % z
if xr + yr >= z:
    d = min(z - xr, z - yr)
else:
    d = 0

print(n, d)
