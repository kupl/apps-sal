n = int(input())
s = '0' + input() + '0'

ok = True
for i in range(1, n + 1):
    if s[i] == '0':
        if s[i - 1] == s[i + 1] == '0':
            ok = False
    else:
        if s[i - 1] == '1' or s[i + 1] == '1':
            ok = False

if ok:
    print("Yes")
else:
    print("No")
