input()
s = input()
ok = True
for i in range(len(s)):
    l = r = True
    if i > 0:
        l = s[i - 1] == '0'
    if i < len(s) - 1:
        r = s[i + 1] == '0'
    if s[i] == '0' and l and r:
        ok = False
    if s[i] == '1' and (not l or not r):
        ok = False
    if not ok:
        break
print('Yes' if ok else 'No')
