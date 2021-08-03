o = input()
e = input()

p = ""

for i in range(len(o)):
    p += o[i]
    if i < len(e):
        p += e[i]

print(p)
