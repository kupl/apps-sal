yes = True
for i in range(8):
    s = input()
    if yes:
        for j in range(7):
            if s[j] == s[j + 1]:
                yes = False
                break
print('YES' if yes else 'NO')
