s = input()
a_idx = None
for i, c in enumerate(list(s)):
    if c == 'A':
        a_idx = i
        break
z_idx = None
for i, c in enumerate(reversed(list(s))):
    if c == 'Z':
        z_idx = len(s) -i
        break
print(len(s[a_idx:z_idx]))
