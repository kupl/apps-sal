s = str(input())
leng = len(s)
ind = s.find('.')
if ind == -1:
    i = 0
    while s[i] == '0':
        i += 1
    s = s[i:]
    if len(s) != 1:
        print(s[0:1] + ('.' + s.strip('0')[1:] if len(s.strip('0')) > 1 else '') + 'E' + str(len(s) - 1))
    else:
        print(s[0:1] + ('.' + s.strip('0')[1:] if len(s.strip('0')) > 1 else ''))
else:
    s = s.strip('0')
    ind = s.find('.')
    i = 0
    while s[i] == '0' or s[i] == '.':
        i += 1
    ind = s.find('.')
    if i >= ind:
        b = ind - i
    else:
        b = ind - 1
    ns = s[0:ind] + s[ind + 1:]
    ns = ns.strip('0')
    if ind != 1:
        print(ns[0:1] + ('.' + ns[1:] if len(ns) > 1 else '') + 'E' + str(b))
    else:
        print(ns[0:1] + ('.' + ns[1:] if len(ns) > 1 else ''))
