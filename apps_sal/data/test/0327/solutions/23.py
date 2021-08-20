(x, y) = [int(x) for x in input().split()]
if y == 1:
    print(x)
else:
    nb = x.bit_length()
    print(2 ** nb - 1)
