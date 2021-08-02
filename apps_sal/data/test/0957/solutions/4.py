s = input()
f = 0
for i in range(len(s)):
    if s[i] == 'h' and f == 0:
        f = 1
    if s[i] == 'e' and f == 1:
        f = 2
    if s[i] == 'i' and f == 2:
        f = 3
    if s[i] == 'd' and f == 3:
        f = 4
    if s[i] == 'i' and f == 4:
        f = 5
        print('YES')
if f < 5:
    print('NO')
