a, b = [], []
for w in input().replace(';', ',').split(','):
    if str.isdigit(w) and (len(w) == 1 or w[0] != '0'):
        a.append(w)
    else:
        b.append(w)
for l in a, b:
    print('"' + ','.join(l) + '"' if l else '-')
