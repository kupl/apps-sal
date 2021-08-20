s = input()
t = input()
s_letters = dict()
t_letters = dict()
CAPS = 'QWERTYUIOPASDFGHJKLZXCVBNM'
SMALLS = 'qwertyuiopasdfghjklzxcvbnm'
for letter in CAPS:
    s_letters[letter] = 0
    t_letters[letter] = 0
for letter in SMALLS:
    s_letters[letter] = 0
    t_letters[letter] = 0
for letter in s:
    s_letters[letter] += 1
for letter in t:
    t_letters[letter] += 1
hurray = 0
hopa = 0
for i in range(26):
    Letter = CAPS[i]
    letter = SMALLS[i]
    tmp = min(s_letters[Letter], t_letters[Letter])
    hurray += tmp
    s_letters[Letter] -= tmp
    t_letters[Letter] -= tmp
    tmp = min(s_letters[letter], t_letters[letter])
    hurray += tmp
    s_letters[letter] -= tmp
    t_letters[letter] -= tmp
    hopa += min(s_letters[Letter] + s_letters[letter], t_letters[Letter] + t_letters[letter])
print(hurray, hopa)
