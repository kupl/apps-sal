(s, x, y) = (input(), 0, 0)
for i in range(len(s)):
    if s[i] == 'x':
        x += 1
    else:
        y += 1
print((x - y) * 'x' if x > y else (y - x) * 'y')
