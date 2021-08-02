a, b, c = input().replace("+", "=").split("=")
lenA = 0
lenB = 0
lenC = 0
a1 = len(a)
b1 = len(b)
c1 = len(c)
st = ""
if (a1 + b1) - c1 == 0:
    st = a + "+" + b + "=" + c
if (a1 + b1) - c1 == 2:
    if a1 > 1:
        lenA = a1 - 1
        lenB = b1
    elif b1 > 1:
        lenB = b1 - 1
        lenA = a1
    lenC = c1 + 1
if (a1 + b1) - c1 == -2:
    if c1 > 1:
        lenA = a1 + 1
        lenB = b1
        lenC = c1 - 1
if lenA and lenB and lenC != 0:
    for x in range(lenA): st = st + "|"
    st = st + "+"
    for x in range(lenB): st = st + "|"
    st = st + "="
    for x in range(lenC): st = st + "|"

if st:
    print(st)
else:
    print("Impossible")
