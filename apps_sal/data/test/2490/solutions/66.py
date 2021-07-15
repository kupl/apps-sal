N = [int(s) for s in input()]
n = len(N)
a = 0
b = 11
for n in N:
    a1 = min(a+n, b+n)
    b1 = min(a+11-n, b+9-n)
    a = a1
    b = b1
print(min(a,b))
