import math

n = int(input().lstrip())
res = 0
poss = []
while bin(n)[2:].find('0') != -1:
    twos = len(bin(n)) - 2
    first_zero = bin(n)[2:].find('0')
    pos = twos - first_zero
    n = n ^ ((2 ** pos) - 1)
    res += 1
    poss.append(pos)
    if bin(n)[2:].find('0') != -1:
        n += 1
        res += 1

print(res)
if poss:
    print(' '.join(map(str, poss)))
