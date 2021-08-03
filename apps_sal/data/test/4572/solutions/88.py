s = sorted(set(input()))
a = len(set(s))
s.append(0)
for i in range(26):
    if s[i] != chr(97 + i):
        print(chr(97 + i))
        break
else:
    print('None')
