s = input()

r = len(s)
c = 1
for i in range(len(s) - 1, 0, -1):
    if s[i] != '0':
        if i > r - i:
            c += 1
            r = i
        elif i == r - i:
            if s[:i] >= s[i:r]:
                c += 1
                r = i
        else:
            break

print(c)
