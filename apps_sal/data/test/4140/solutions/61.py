s = input()
(b, w) = (0, 0)
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            w += 1
        else:
            b += 1
    elif s[i] == '0':
        b += 1
    else:
        w += 1
print(min(b, w))
