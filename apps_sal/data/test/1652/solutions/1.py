s = input()
i = 0
n = len(s)
while i < n:
    if s[i:i + 10] == 'dreamerase':
        i += 5
    elif s[i:i + 7] == 'dreamer':
        i += 7
    elif s[i:i + 5] == 'dream':
        i += 5
    elif s[i:i + 6] == 'eraser':
        i += 6
    elif s[i:i + 5] == 'erase':
        i += 5
    else:
        break
print('YES' if i == n else 'NO')
