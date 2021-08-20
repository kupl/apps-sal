o = input()
e = input()
pw = ''
for i in range(len(o)):
    pw += o[i]
    if i < len(e):
        pw += e[i]
print(pw)
