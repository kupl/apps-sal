s = input()
t = input()
a = 0
for i in range(3):
    if s[i] != t[-i - 1]:
        a = 1
print('YES' if a == 0 else 'NO')
