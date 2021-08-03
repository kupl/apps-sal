from collections import Counter
s = input()
c = 0
p = 0
cd = 0
for i in range(len(s)):
    if s[i] == 'R' and (p == 0 or c != 0):
        c += 1
        p = 1
    else:
        cd = max(cd, c)
        c = 0
print(max(cd, c))
