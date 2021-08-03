orph = ['a', 'e', 'i', 'o', 'u']
string = input()
ctr = 0
out = ''
for i, c in enumerate(string):
    if c in orph:
        ctr = 0
    else:
        ctr += 1
        if ctr > 2:
            if not (c == string[i - 1] and c == string[i - 2]):
                out = out + ' '
                ctr = 1
    out = out + c
print(out)
