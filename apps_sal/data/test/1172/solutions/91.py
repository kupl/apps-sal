D = [0, 0, 0, 1, 0]
for s in input(): D = [(D[j] * ((s == "?") * 2 + 1) + D[j + 1] * (s in t + "?")) % (10**9 + 7) for j, t in enumerate("CBA.")] + [0]
print(D[0])
