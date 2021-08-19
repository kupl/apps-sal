(s, c) = ('heidi', 0)
for i in input():
    if i == s[c]:
        c += 1
    if c == 5:
        break
print('YES' if c == 5 else 'NO')
