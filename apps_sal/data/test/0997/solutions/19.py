from math import ceil, modf
s = input().replace(",", ";")
s = s.split(";")
a = []
b = []
for i in s:
    try:
        d = str(int(i))
        if len(i) > 1 and i[0] == "0" or i[0] == "-":
            b.append(i)
        else:
            a.append(d)
    except ValueError:
        b.append(i)
if a:
    print('"' + ",".join(a) + '"')
else:
    print("-")
if b:
    print('"' + ",".join(b) + '"')
else:
    print("-")
