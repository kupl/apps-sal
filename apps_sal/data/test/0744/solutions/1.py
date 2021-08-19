n = int(input())
s = input()
sf = 0
fs = 0
for i in range(1, n):
    if s[i] == 'F' and s[i - 1] == 'S':
        sf += 1
    elif s[i] == 'S' and s[i - 1] == 'F':
        fs += 1
if sf > fs:
    print('YES')
else:
    print('NO')
