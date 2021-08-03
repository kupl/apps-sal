o = input()
e = input()
p = ''
if len(o) == len(e):
    for i in range(0, len(o)):
        p += o[i] + e[i]

elif len(o) >= len(e):
    for i in range(0, len(e)):
        p += o[i] + e[i]
    p += o[-1]

print(p)
