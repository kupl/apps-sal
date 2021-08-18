n = int(input())

isC = False
isB = False
isA = False

d = {}

for i in range(n):
    line = input()

    c = int(line.split(' ')[0])
    s = line.split(' ')[1]

    if 'A' in s:
        isA = True

    if 'B' in s:
        isB = True

    if 'C' in s:
        isC = True

    name = ''.join(sorted(s))

    try:
        d[name] = min(c, d[name])

    except:
        d[name] = c

if not isA or not isB or not isC:
    print(-1)

else:
    arr = []

    try:
        arr.append(d['A'] + d['B'] + d['C'])
    except:
        pass

    try:
        arr.append(d['A'] + d['BC'])
    except:
        pass

    try:
        arr.append(d['AB'] + d['C'])
    except:
        pass

    try:
        arr.append(d['AC'] + d['B'])
    except:
        pass

    try:
        arr.append(d['AB'] + d['BC'])
    except:
        pass

    try:
        arr.append(d['AC'] + d['BC'])
    except:
        pass

    try:
        arr.append(d['AB'] + d['AC'])
    except:
        pass

    try:
        arr.append(d['ABC'])
    except:
        pass

    try:
        arr.append(d['ABC'])
    except:
        pass

    print(min(arr))
