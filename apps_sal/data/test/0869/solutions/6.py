(r, b) = [int(i) for i in input().split()]
(p, q) = (min(r, b), max(r, b))
print(p, (q - p) // 2)
