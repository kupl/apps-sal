N = [int(s) for s in input()]
M = len(N)

eq = 0
ov = 1

for n in N:
    a = min(eq + n, ov + 10 - n)
    b = min(eq + (n + 1), ov + 10 - (n + 1))
    eq, ov = a, b

print(eq)
