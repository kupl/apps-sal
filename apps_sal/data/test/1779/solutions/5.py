s1 = input()
s2 = input()
s = input()
res = ""
for x in s:
    if 'A' <= x <= 'Z':
        res += s2[s1.index(x.lower())].upper()
    elif 'a' <= x <= 'z':
        res += s2[s1.index(x)]
    else:
        res += x
print(res)
