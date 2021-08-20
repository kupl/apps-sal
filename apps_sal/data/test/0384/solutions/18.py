input()
sl = []
k = 0
for cell in input():
    if cell == 'B':
        k += 1
    else:
        if k > 0:
            sl.append(str(k))
        k = 0
if k > 0:
    sl.append(str(k))
print(len(sl))
print(' '.join(sl))
