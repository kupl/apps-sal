s = input()
f = 0
l = input().split()
for i in l:
    if i[0] == s[0] or s[1] == i[1]:
        f = 1
print('YES' if f else 'NO')

