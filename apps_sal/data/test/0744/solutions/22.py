n = int(input())
s = input()
S = 0
F = 0
for i in range(1, n):
    if s[i] == 'S':
        if s[i - 1] == 'F':
            S += 1
    elif s[i - 1] == 'S':
        F += 1
if F > S:
    print('YES')
else:
    print('NO')
