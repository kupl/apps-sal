s = input()
t = input()
sc = [0] * 26
tc = [0] * 26
for i in range(len(s)):
    sc[ord(s[i]) - ord('a')] += 1
    tc[ord(t[i]) - ord('a')] += 1
sc.sort()
tc.sort()
if tuple(sc) == tuple(tc):
    print('Yes')
else:
    print('No')
