s = input()
fst = s[:s.index('e')]
to_move = int(s[s.index('e') + 1:])
curr = 0
while curr != to_move:
    if fst[-1] == '.':
        fst = fst[:-1] + '0.'
    else:
        prt = fst.split('.')
        fst = prt[0] + prt[1][0] + '.' + prt[1][1:]
    curr += 1
if fst[-1] == '.':
    fst = fst[:-1]
test = fst.split('.')
if len(test) != 1 and set(test[-1]) == {'0'}:
    fst = test[0]
print(fst)
