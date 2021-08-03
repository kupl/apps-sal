
O = input()
E = input()

i = 0
for i in range(len(O)):
    print(O[i], end='')
    if i < len(E):
        print(E[i], end='')
    i += 1
