h1, a1, c = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))

turn = 0
l = list()

while ((h1 > 0) and (h2 > 0)):
    if (turn % 2 == 0):
        if (h1 > a2) or (h2 <= a1):
            l.append('STRIKE')
            h2 -= a1
        else:
            l.append('HEAL')
            h1 += c
    else:
        h1 -= a2

    turn += 1

print(len(l))
print('\n'.join(l))

