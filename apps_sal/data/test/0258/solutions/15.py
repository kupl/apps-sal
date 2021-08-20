n = int(input())
s = input()
fer = 0
f = 0
l = 0
ler = 0
for i in range(int(n / 2)):
    if s[i] == '?':
        fer += 1
    else:
        f += int(s[i])
for i in range(int(n / 2), n):
    if s[i] == '?':
        ler += 1
    else:
        l += int(s[i])
if (fer + ler) % 2:
    print('Monocarp')
elif f < l:
    if l - f == 9 * ((fer - ler) / 2):
        print('Bicarp')
    else:
        print('Monocarp')
elif f - l == 9 * ((ler - fer) / 2):
    print('Bicarp')
else:
    print('Monocarp')
