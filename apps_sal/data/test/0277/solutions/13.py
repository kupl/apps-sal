import math as m
(n, a, b) = [int(x) for x in input().split()]
if a > b:
    (a, b) = (b, a)
rounds = int(m.log2(n))
mr = rounds
(lft, rgt) = (1, n)
while True:
    mdl = (lft + rgt) // 2
    if a <= mdl and b > mdl:
        break
    rounds -= 1
    if a <= mdl and b <= mdl:
        rgt = mdl
    elif a > mdl and b > mdl:
        lft = mdl + 1
if rounds == mr:
    print('Final!')
else:
    print(rounds)
