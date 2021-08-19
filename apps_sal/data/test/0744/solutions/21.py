n = int(input())
s = input()
fs = 0
sf = 0
for i in range(1, len(s)):
    if s[i] == 'F' and s[i - 1] == 'S':
        sf += 1
    elif s[i] == 'S' and s[i - 1] == 'F':
        fs += 1
if sf > fs:
    print('YES')
else:
    print('NO')
