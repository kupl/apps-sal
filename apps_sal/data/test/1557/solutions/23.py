h1, a1, c1 = [int(x) for x in input().split()]
h2, a2 = [int(x) for x in input().split()]

n_rounds = 0
things_to_do = []

while(h2 > 0):
    n_rounds += 1
    if h2 <= a1 or h1 > a2:
        things_to_do.append('STRIKE')
        h2 -= a1
        h1 -= a2
    else:
        things_to_do.append('HEAL')
        h1 += c1
        h1 -= a2

print(n_rounds)
for i in things_to_do:
    print(i)
