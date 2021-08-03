s = input()
pref = [s[0]]
for i in range(1, len(s)):
    pref.append(min(pref[i - 1], s[i]))
for k in range(len(s)):
    if pref[k] >= s[k]:
        print('Mike')
    else:
        print('Ann')
