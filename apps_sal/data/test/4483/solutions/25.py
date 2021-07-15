with open(0) as f:
    x, a, b = map(int, f.read().split())
print(x - a - (x-a)//b*b)
