s = input()
for i in range(len(s)):
    if s.count(s[i]) % 2 != 0:
        print('No')
        return
print('Yes')
