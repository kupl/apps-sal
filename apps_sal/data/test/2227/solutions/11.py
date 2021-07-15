from re import findall
h, acc = 0, 0
for i in findall('heavy|metal', input()):
    if i.startswith('h'): h += 1
    else: acc += h
print(acc)
