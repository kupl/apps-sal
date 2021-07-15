n = sum([{'x':1, 'y':-1}[c] for c in input()])
print(n * 'x' if n > 0 else -n * 'y')

