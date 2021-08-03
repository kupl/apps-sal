s = input()
heavy = 0
total = 0

i = 0
while i < len(s) - 4:
    if s[i:i + 5] == 'heavy':
        i += 5
        heavy += 1
    elif s[i:i + 5] == 'metal':
        i += 5
        total += heavy
    else:
        i += 1


print("%d" % total)
