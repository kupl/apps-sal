n = int(input())
s = input()
sf = 0
fs = 0
last = s[0]
for i in range(n):
    if s[i] != last:
        if last == 'F':
            fs += 1
        else:
            sf += 1
        last = s[i]
if sf > fs:
    print('YES')
else:
    print('NO')
