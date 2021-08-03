s = input()

m = -1
for x in zip(s[0:], s[1:], s[2:]):
    number = abs(753 - int("".join(x)))
    if m < 0:
        m = number
    elif number < m:
        m = number

print(m)
