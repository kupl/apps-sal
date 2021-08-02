n = int(input())
s = input()
ok = True
for i in range(len(s) - 1):
    if s[i] == '1' and s[i + 1] == '1':
        ok = False
    if i + 2 < len(s):
        if s[i] == '0' and s[i + 1] == '0' and s[i + 2] == '0':
            ok = False
if len(s) >= 2:
    if s[0] == '0' and s[1] == '0':
        ok = False
    if s[-1] == '0' and s[-2] == '0':
        ok = False
else:
    ok = (s[0] == '1')
print('Yes' if ok else 'No')
