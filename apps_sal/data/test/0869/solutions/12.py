(a, b) = [int(x) for x in input().split()]
(a, b) = (min(a, b), max(a, b))
print(a, (b - a) // 2)
