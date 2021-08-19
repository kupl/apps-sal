o = input()
e = input()
d = ''
if len(o) == len(e):
    for i in range(len(o)):
        d += o[i]
        d += e[i]
    print(d)
else:
    for i in range(len(e)):
        d += o[i]
        d += e[i]
    d += o[-1]
    print(d)
