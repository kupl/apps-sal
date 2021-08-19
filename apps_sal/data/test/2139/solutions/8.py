s = input()
k = 0
l = 0
sstr = -2
count = 0
while sstr != -1:
    sstr = s.find('bear')
    if sstr == -1:
        break
    elif sstr == 0 or sstr == len(s) - 1:
        k += len(s) - 3
    else:
        z = (sstr + 1) * (len(s) - sstr - 3)
        k += z
    s = s[sstr + 1:len(s)]
print(k)
