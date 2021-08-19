(x, y, z) = list(map(int, input().split()))
a = z - x % z
b = z - y % z
p = x // z + y // z
q = 0
if a <= y:
    p1 = (x + a) // z + (y - a) // z
    if p1 > p:
        (p, q) = (p1, a)
if b < x:
    p2 = (x - b) // z + (y + b) // z
    if p2 > p or (p2 == p and b < q):
        (p, q) = (p2, b)
print(p, q)
