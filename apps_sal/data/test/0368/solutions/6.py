desk = [list(input()) for i in range(8)]
C = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0, '.': 0}
p1 = 0
p2 = 0
for x in desk:
    for x2 in x:
        if x2.isupper():
            p2 += C[x2.lower()]
        else:
            p1 += C[x2]
if p1 == p2:
    print('Draw')
else:
    print('White' if p2 > p1 else 'Black')
