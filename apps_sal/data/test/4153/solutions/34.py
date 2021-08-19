S = input()
o = 0
i = 0
for j in S:
    if j == '0':
        o += 1
    else:
        i += 1
print(min(o, i) * 2)
