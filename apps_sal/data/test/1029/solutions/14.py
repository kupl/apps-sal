def cmp(x, y):
    for i in range(min(len(x), len(y))):
        if x[i] < y[i]:
            return True
    return len(x) < len(y)


s = input()
r, c = len(s), 1
for i in range(len(s) - 1, 0, -1):
    if s[i] != '0':
        if i > r - i:
            c += 1
            r = i
        elif i == r - i:
            if not cmp(s[:i], s[i:r]):
                c += 1
                r = i
        else:
            break
print(c)
