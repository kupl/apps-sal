s = input()
n = len(s)
(x, y) = (0, 0)
for i in range(n):
    if i % 2 == 0:
        if s[i] == '0':
            y += 1
        else:
            x += 1
    elif s[i] == '0':
        x += 1
    else:
        y += 1
print(min(x, y))
