a = input()
l = []
mi = 999999999999999
for i in a:
    k = ord(i) - 97
    if k > mi:
        l.append('1')
    else:
        l.append('0')
        mi = k
for i in l:
    print(i.replace('1', 'Ann').replace('0', 'Mike'))
