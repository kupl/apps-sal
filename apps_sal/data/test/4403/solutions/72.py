l = input()
s = 0
for c in l:
    if c == '+':
        s += 1
    elif c == '-':
        s -= 1
print(s)
