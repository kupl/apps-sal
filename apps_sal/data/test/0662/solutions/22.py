n = int(input())
(ind1, ind2) = (1, 2)
indicator = True
for i in range(n):
    a = int(input())
    if a != ind1 and a != ind2:
        indicator = False
        print('NO')
        break
    else:
        (ind1, ind2) = (a, 6 - (ind1 + ind2))
if indicator:
    print('YES')
