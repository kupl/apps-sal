s = input()
s = sorted(s)
dif = True
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dif = False
print('yes' if dif else 'no')
