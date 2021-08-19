(a, b, ab) = [int(x) for x in input().split()]
if a > b:
    print(2 * ab + 2 * b + 1)
elif a == b:
    print(2 * ab + 2 * a)
else:
    print(1 + 2 * ab + 2 * a)
