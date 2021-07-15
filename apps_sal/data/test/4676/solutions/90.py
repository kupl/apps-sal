o = input()
e = input()
s = ""
for i in range(len(e)):
    s += o[i]
    s += e[i]
if len(o) == len(e):
    print(s)
else :
    s += o[-1]
    print(s)
