items = ['A', 'C', 'G', 'T']


def max(a, b):
    return a if a > b else b


x = 0
y = 0
for c in list(input()):
    if c in items:

        y += 1
        x = max(x, y)
    else:
        y = 0
print(x)
