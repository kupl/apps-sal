n = int(input())
s = input()
s += ' '
col = 0
i = 0
while i != n:
    if (s[i] == 'U' and s[i + 1] == 'R') or (s[i] == 'R' and s[i + 1] == 'U'):
        col += 1
        i += 2

    else:
        i += 1
        col += 1
print(col)
