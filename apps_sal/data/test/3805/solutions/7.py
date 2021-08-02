a = []
for ch in input():
    if a and a[-1] == ch:
        a.pop()
    else:
        a.append(ch)
print('Yes' if not a else 'No')
