s = input()

p = 0
r = 'no'
for d in reversed(s):
    if d == '0':
        p += 1
    elif p >= 6:
        r = 'yes'

print(r)
