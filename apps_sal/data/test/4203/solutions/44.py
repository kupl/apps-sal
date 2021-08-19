S = input()
b = False
if S[0] == 'A' and S[2:-1].count('C') == 1:
    c = 0
    for s in S:
        if s.isupper():
            c += 1
    if c == 2:
        b = True
print('AC' if b else 'WA')
