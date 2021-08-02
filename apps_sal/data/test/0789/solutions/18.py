s = input()
r = 1 if s[0] == '4' else 2
for c in s[1:]:
    if c == '4':
        r = r * 2 + 1
    else:
        r = r * 2 + 2
print(r)
