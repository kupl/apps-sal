n = int(input())
s = input()
a = 0
b = 0
for i in range(n - 1):
    if s[i] == 'S' and s[i + 1] == 'F':
        a += 1
    elif s[i] == 'F' and s[i + 1] == 'S':
        b += 1
if a > b:
    print('YES')
else:
    print('NO')
