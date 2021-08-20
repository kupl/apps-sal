input()
pos = [c == 'X' for c in input()]
b = pos.count(True) - len(pos) // 2
print(abs(b))
if b < 0:
    for p in range(len(pos)):
        if not pos[p]:
            pos[p] = True
            b += 1
            if b == 0:
                break
elif b > 0:
    for p in range(len(pos)):
        if pos[p]:
            pos[p] = False
            b -= 1
            if b == 0:
                break
print(''.join(('X' if p else 'x' for p in pos)))
