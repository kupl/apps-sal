n = input()
a = []
for i in range(len(n)):
    if n[i] not in a:
        a.append(n[i])
if len(a) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
