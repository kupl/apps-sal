# Fast IO (be careful about bytestring)

# import os,io
# input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


for _ in range(int(input())):
    a, b, x, y, n = list(map(int, input().split()))
    if a + b - x - y < n:
        print(x * y)
    else:
        minProduct = 10 ** 20
        # Decreasing a first
        if a - n >= x:
            product = (a - n) * b
            if product < minProduct:
                minProduct = product
        else:
            product = x * max(y, b - n + a - x)
            if product < minProduct:
                minProduct = product
        # Decreasing b first
        if b - n >= y:
            product = (b - n) * a
            if product < minProduct:
                minProduct = product
        else:
            product = y * max(x, a - n + b - y)
            if product < minProduct:
                minProduct = product
        print(minProduct)
