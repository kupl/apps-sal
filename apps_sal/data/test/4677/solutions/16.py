S = input()
F = []
for ch in S:
    if ch == 'B':
        if len(F) > 0:
            F.pop()
    else:
        F.append(ch)
print(''.join(F))
