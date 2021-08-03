sa = input()
sa2 = 0
homes = []
aways = []
for x in range(int(sa)):
    tt = input().split(' ')
    homes.append(int(tt[0]))
    aways.append(int(tt[1]))
for element in homes:
    for element2 in aways:
        if element == element2:
            sa2 += 1

print(sa2)
