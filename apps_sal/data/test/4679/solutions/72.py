sa = input() + 'a'
sb = input() + 'b'
sc = input() + 'c'
st = 'a'
a = 0
b = 0
c = 0
while a < len(sa) and b < len(sb) and c < len(sc):
    if st == 'a':
        st = sa[a]
        a += 1
    elif st == 'b':
        st = sb[b]
        b += 1
    else:
        st = sc[c]
        c += 1
if a == len(sa):
    print('A')
elif b == len(sb):
    print('B')
else:
    print('C')
