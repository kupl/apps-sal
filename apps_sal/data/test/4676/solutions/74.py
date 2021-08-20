o = input()
e = input()
a = ''
for i in range(len(o)):
    a += o[i]
    if i < len(e):
        a += e[i]
print(a)
