(n, x, y) = input().split(' ')
troops = []
for i in range(int(n)):
    (a, b) = input().split(' ')
    troops.append([int(a) - int(x), int(b) - int(y)])
s = set()
for troop in troops:
    if troop[0] != 0:
        s.add(troop[1] / troop[0])
    else:
        s.add(1000000)
print(len(s))
