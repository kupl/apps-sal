n = int(input())
s = input()
a = ''
t = 'aeiouy'
for i in range(n):
    if t.find(s[i]) < 0:
        a = a + s[i]
    elif i > 0 and s[i] != s[i - 1] or i == 0:
        a = a + s[i]
    elif i > 0 and s[i] == 'e' and (i < n - 1 and s[i + 1] != s[i] or i == n - 1) and (i > 1 and s[i - 2] != s[i] or i <= 1):
        a = a + s[i]
    elif i > 0 and s[i] == 'o' and (i < n - 1 and s[i + 1] != s[i] or i == n - 1) and (i > 1 and s[i - 2] != s[i] or i <= 1):
        a = a + s[i]
print(a)
'\n13\npobeeeedaaaaa\npobeda\n22\niiiimpleeemeentatiioon\nimplemeentatioon\n18\naeiouyaaeeiioouuyy\naeiouyaeeioouy\n24\naaaoooiiiuuuyyyeeeggghhh\naoiuyeggghhh\n'
