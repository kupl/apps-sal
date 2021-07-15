s = input()
g = 0
p = 0
for i in s:
    if i == "g":
        g += 1
    else:
        p += 1
print(((g-p)//2))

