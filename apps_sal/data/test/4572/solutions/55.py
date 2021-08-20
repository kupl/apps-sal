a = input()
s = [0] * 26
for i in range(len(a)):
    s[ord(a[i]) - 97] = 1
if sum(s) == 26:
    print('None')
else:
    print(chr(s.index(min(s)) + 97))
