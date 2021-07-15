s = input().strip()
t = input().strip()
ok = 0
vow = 'aeiou'
if len(s) == len(t):
    ok = 1
    for a, b in zip(s, t):
        if (a in vow) ^ (b in vow):
            ok = 0
            break
print('Yes' if ok else 'No')

