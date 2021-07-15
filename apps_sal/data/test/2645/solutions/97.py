s = input()
gp = [1, 0]
p = 0
if s[0] == 'p':
    p -= 1
for i in range(1, len(s)):
    if s[i] == 'g':
        if gp[0] > gp[1]:
            gp[1] += 1
            p += 1
        else:
            gp[0] += 1
    if s[i] == 'p':
        if gp[0] > gp[1]:
            gp[1] += 1
        else:
            gp[0] += 1
            p -= 1
print(p)
