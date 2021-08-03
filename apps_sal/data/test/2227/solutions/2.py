z = r = 0
for w in input().split("heavy"):
    r += w.count("metal") * z
    z += 1
print(r)
