s1 = input() + input()[::-1]
s2 = input() + input()[::-1]
s1 = s1[:s1.find('X')] + s1[s1.find('X') + 1:]
s2 = s2[:s2.find('X')] + s2[s2.find('X') + 1:]
flag = False
for i in range(3):
    if s1 == s2:
        flag = True
        break
    s1 = s1[-1] + s1[:-1]
print('YES' if flag else 'NO')
