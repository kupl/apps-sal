import sys

n = int(input())
lamps = input()

if len(lamps) == 1:
    print(0)
    print(lamps)
    return


def other(c1, c2='R'):
    if 'G' != c1 and 'G' != c2:
        return 'G'
    elif 'R' != c1 and 'R' != c2:
        return 'R'
    else:
        return 'B'


newlamps = list(lamps)
i = 1
recolors = 0
while i < n - 1:
    if newlamps[i] == newlamps[i - 1]:
        recolors += 1
        newlamps[i] = other(newlamps[i - 1], newlamps[i + 1])
    i += 1

if newlamps[-1] == newlamps[-2]:
    newlamps[-1] = other(newlamps[-2])
    recolors += 1

print(recolors)
print(''.join(newlamps))
