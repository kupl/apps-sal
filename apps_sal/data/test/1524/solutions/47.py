S = input()
lsS = list(S)
ls = []
ii = 0
mode = 'R'
for i in lsS:
    if i == 'R' and mode == 'R':
        ii += 1
    elif i == 'L' and mode == 'R':
        ls.append(ii)
        mode = 'L'
        ii = 1
    elif i == 'L' and mode == 'L':
        ii += 1
    elif i == 'R' and mode == 'L':
        ls.append(ii)
        mode = 'R'
        ii = 1
ls.append(ii)
lsans = [0] * len(S)
index = -1
for i in range(len(ls)):
    if i % 2 == 0:
        index += ls[i]
        lsans[index + 1] += ls[i] // 2
        lsans[index] += ls[i] - ls[i] // 2
    else:
        lsans[index] += ls[i] // 2
        lsans[index + 1] += ls[i] - ls[i] // 2
        index += ls[i]
ans = [str(i) for i in lsans]
print(' '.join(ans))
