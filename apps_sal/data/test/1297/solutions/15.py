s = input()
nb = 1
n = 0
for i in range(len(s) - 1):
    if s[i] != s[i + 1] and nb % 2 == 0:
        n += 1
        nb = 1
    elif s[i] != s[i + 1]:
        nb = 1
    else:
        nb += 1
if nb % 2 == 0:
    print(n + 1)
else:
    print(n)
