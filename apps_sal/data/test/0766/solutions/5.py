a = [0] * 27
x = input()
for i in x:
    a[ord(i) - 96] += 1
s = 0
q = 0
for i in a:
    if i != 0:
        s += 1
    if i > 1:
        q += 1
if s > 4:
    print('No')
elif s <= 1:
    print('No')
elif s == 4:
    print('Yes')
elif s == 2:
    if q >= 2:
        print('Yes')
    else:
        print('No')
elif q >= 1:
    print('Yes')
else:
    print('No')
