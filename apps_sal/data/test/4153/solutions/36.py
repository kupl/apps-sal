s = input()

z = 0
o = 0
for c in s:
    if c == '1':
        o += 1
    else:
        z += 1

print((min(o, z) * 2))

