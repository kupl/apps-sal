s = input()

ans = True

for c in s[0::2]:
    if c not in {'R', 'U', 'D'}:
        ans = False
        break

for c in s[1::2]:
    if c not in {'L', 'U', 'D'}:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')
