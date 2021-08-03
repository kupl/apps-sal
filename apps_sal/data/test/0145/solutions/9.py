s = input()
d = set()
for i in s:
    if i not in d:
        d.add(i)
if len(d) % 2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
