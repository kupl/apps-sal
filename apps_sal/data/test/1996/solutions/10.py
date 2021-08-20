q = int(input())
d = set([chr(i) for i in range(97, 123)])
gf = 0
for i in range(0, q - 1):
    s = input()
    s1 = s[2:]
    if s[0] == '!':
        if len(d) == 1:
            gf += 1
        d &= set(s1)
    elif s[0] == '.':
        d = d.difference(set(s1))
    else:
        if len(d) == 1:
            gf += 1
        d = d.difference(set(s1))
s = input()
print(gf)
