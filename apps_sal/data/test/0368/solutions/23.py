import string
(wp, bp) = (0, 0)
for i in range(8):
    inStr = input()
    for p in list(inStr):
        if not p == '.':
            lp = p.lower()
            points = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1, 'k': 0}[lp]
            if not p.islower():
                wp = wp + points
            else:
                bp = bp + points
wp > bp and print('White') or (wp == bp and print('Draw')) or (wp < bp and print('Black'))
