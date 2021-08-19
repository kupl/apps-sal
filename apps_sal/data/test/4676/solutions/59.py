(o, e) = [input() for i in range(2)]
for i in range(len(e)):
    print(o[i], end='')
    print(e[i], end='')
if len(o) - len(e) == 1:
    print(o[len(o) - 1])
