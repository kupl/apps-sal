o = str(input())
e = str(input())
a = ''
for i in range(len(e)):
    a += o[i]
    a += e[i]
    if len(o) != len(e) and i == len(e) - 1:
        a += o[i + 1]
print(a)
