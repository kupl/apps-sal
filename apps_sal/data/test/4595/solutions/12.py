import math
b = input()
c = []
for i in b:
    c.append(i)

a1 = c[c.index("A"):]
a2 = [i for i, x in enumerate(a1) if x == "Z"]
print(len(a1[:a2[-1] + 1]))
