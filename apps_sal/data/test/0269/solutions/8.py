s = input()

a = ['*'] * 4

for i, c in enumerate(s):
    if c != '!':
        a[i % 4] = c

answ = dict(R=0, G=0, B=0, Y=0)
for i in range(len(s)):
    if s[i] == '!':
        answ[a[i % 4]] += 1

print(answ['R'], answ['B'], answ['Y'], answ['G'],)
