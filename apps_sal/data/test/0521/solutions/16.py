n = int(input())
s = input()
x = False
dup = False
for i in range(0, n - 1):
    if s[i] == s[i + 1] and s[i] != '?':
        dup = True
        break
for i in range(0, n):
    if x:
        break
    if s[i] == '?':
        if i == 0:
            x = True
            continue
        elif i == n - 1:
            x = True
            continue
        else:
            a = s[i - 1]
            b = s[i + 1]
            if a == '?' or b == '?':
                x = True
                continue
            elif a == b:
                x = True
                continue
            else:
                continue
if dup:
    print('No')
elif x:
    print('Yes')
else:
    print('No')
