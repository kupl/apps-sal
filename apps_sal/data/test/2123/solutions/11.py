

n = int(input())

heights = input()
splitted = heights.split(' ')
splitted.reverse()
splitted.append('0')
splitted.reverse()

energy = 0
dollars = 0

for i in range(0, len(splitted) - 1):
    h = int(splitted[i])
    hplus = int(splitted[i + 1])

    diff = hplus - h

    if diff > energy:
        dollars += (diff - energy)
        energy = 0
    else:
        energy -= diff

print(dollars)
