pointer = 0

s = input()
c = 0
for x in s:
    k = ord(x) - ord('a')
    crr = []
    if(k - pointer >= 0):
        crr.append(k - pointer)
    else:
        crr.append(k - pointer + 26)
    if(pointer - k >= 0):
        crr.append(pointer - k)
    else:
        crr.append(pointer - k + 26)
    pointer = k
    c += min(crr)
print(c)
