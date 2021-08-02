c = 0
for i in range(8):
    s = input()
    for j in range(len(s) - 1):
        if s[j] == s[j + 1]:
            c += 1
            break
if c == 0:
    print('YES')
else:
    print('NO')
