s = input()
n = len(s)
idx = 0
while idx < n:
    if idx + 5 > n:
        break
    if s[idx:idx + 5] == 'dream':
        idx += 5
        if idx + 2 <= n and s[idx:idx + 2] == 'er' and (idx + 2 == n or s[idx + 2:idx + 3] != 'a'):
            idx += 2
    elif s[idx:idx + 5] == 'erase':
        idx += 5
        if idx + 1 <= n and s[idx:idx + 1] == 'r':
            idx += 1
    else:
        break
if idx == n:
    print('YES')
else:
    print('NO')
