s = input()
t = input()

cycle_to = [''] * 26
cycle_from = [''] * 26

for i in range(len(s)):
    if cycle_to[ord(s[i]) - 97] == t[i]:
        continue
    if cycle_to[ord(s[i]) - 97] == '':
        cycle_to[ord(s[i]) - 97] = t[i]
    else:
        print('No')
        break
    
    if cycle_from[ord(t[i]) - 97] == s[i]:
        continue
    if cycle_from[ord(t[i]) - 97] == '':
        cycle_from[ord(t[i]) - 97] = s[i]
    else:
        print('No')
        break
else:
    print('Yes')
