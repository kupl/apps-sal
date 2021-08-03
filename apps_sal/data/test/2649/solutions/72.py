_, *Z = open(0)
A, B = [], []
for z in Z:
    x, y = map(int, z.split())
    A += [x + y]
    B += [x - y]
print(max(max(A) - min(A), max(B) - min(B)))
