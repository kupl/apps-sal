s = input()
t = input()
a = 0
for i in range(len(s)):
    if s[i] == t[i]:
        a += 1
if a == len(s):
    print('Yes')
else:
    print('No')
