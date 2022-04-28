s = bin(int(input()))[2:].zfill(6)
l = []
for i in [0, 5, 3, 2, 4, 1]:
    l.append(s[i])
print(int(''.join(l), 2))
