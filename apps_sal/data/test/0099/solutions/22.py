b, q, l, m = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
if abs(b) > l:
    c = 0
elif b == 0:
    if 0 in a: c = 0
    else: c = "inf"
elif q == 1:
    if b in a: c = 0
    else: c = "inf"
elif q == -1:
    if b in a and -b in a: c = 0
    else: c = "inf"
elif q == 0:
    if 0 not in a: c = "inf"
    elif b in a: c = 0
    else: c = 1
else:
    c = 0
    while abs(b) <= l:
        if b not in a: c += 1
        b *= q
print(c)
