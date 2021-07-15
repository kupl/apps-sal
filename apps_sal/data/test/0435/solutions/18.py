le, ch = map(int, input().split())
st = input()
ca, cb, si, mx = [0] * 4
for x in st:
    if x == 'a':
        ca += 1
    else:
        cb += 1
    if min(ca, cb) > ch:
        if st[si] == 'a':
            ca -= 1
        else:
            cb -= 1
        si += 1
    else:
        mx += 1
print(mx)
