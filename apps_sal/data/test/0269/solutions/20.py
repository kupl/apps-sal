g = input()
c1 = g[0::4]
c2 = g[1::4]
c3 = g[2::4]
c4 = g[3::4]
colors = ['R', 'B', 'Y', 'G']
broken1 = 0
broken2 = 0
broken3 = 0
broken4 = 0
letters = []
for item in c1:
    if item == '!':
        broken1 += 1
    else:
        if item not in letters:
            letters.append(item)
for item in c2:
    if item == '!':
        broken2 += 1
    else:
        if item not in letters:
            letters.append(item)
for item in c3:
    if item == '!':
        broken3 += 1
    else:
        if item not in letters:
            letters.append(item)
for item in c4:
    if item == '!':
        broken4 += 1
    else:
        if item not in letters:
            letters.append(item)
answer = {letters[0]: broken1, letters[1]: broken2,letters[2]: broken3,letters[3]: broken4}
print(answer['R'],answer['B'],answer['Y'],answer['G'])

