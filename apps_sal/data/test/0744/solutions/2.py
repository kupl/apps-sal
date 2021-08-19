n = int(input())
s = input()
(c1, c2) = (0, 0)
for i in range(1, n):
    if s[i - 1] == 'S' and s[i] == 'F':
        c1 += 1
    elif s[i - 1] == 'F' and s[i] == 'S':
        c2 += 1
if c1 > c2:
    print('YES')
else:
    print('NO')
