S = input()
z = 0
o = 0
for c in S:
    if c == '0':
        z += 1
    else:
        o += 1
print(min([z,o])*2)
