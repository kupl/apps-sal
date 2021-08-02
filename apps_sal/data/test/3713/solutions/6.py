l, s = int(input()), input()
x, y = 0, 1
for i in range(l - 1):
    if s[i] == s[i + 1]:
        x += 1
    else: y += 1
print(y + min(2, x))
