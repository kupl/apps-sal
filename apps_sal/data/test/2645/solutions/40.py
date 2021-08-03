s = input()

gs = 0
ps = 0

for ss in s:
    if ss == 'g':
        gs += 1
    else:
        ps += 1

print(max(0, (gs - ps) // 2))
