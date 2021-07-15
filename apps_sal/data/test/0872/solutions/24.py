r = int(input())
mass = [int(i) for i in input().split()]
c = False
n = False
for i in mass:
    if i % 2 == 0:
        c = True
    else:
        n = True
if c and n:
    print(*sorted(mass))
else:
    print(*mass)
