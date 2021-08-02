s = input()
r = set(map(chr, range(97, 97 + 26)))
r = r - set(s)
if len(r) == 0:
    print('None')
else:
    r = min(r)
    print(r)
