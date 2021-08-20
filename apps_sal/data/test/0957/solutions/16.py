a = input()
j = 0
s = 'heidi#'
for i in a:
    if i == s[j]:
        j += 1
print('YES' if j == 5 else 'NO')
