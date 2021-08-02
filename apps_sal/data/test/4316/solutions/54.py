s = input()
for i in range(len(s)):
    if s.count(s[i]) != 2:
        print('No')
        break
else:
    print('Yes')
