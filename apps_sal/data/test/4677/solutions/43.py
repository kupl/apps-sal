s = input()

out = ''
for x in s:
    if x != 'B':
        out += x
    else:
        if out == '':
            continue
        else:
            out = out[:-1]
print(out)
