s = input()
ans = 1
used = list('ABCDEFGHIJ')
if s[0] == '?':
    ans *= 9
elif s[0] in used:
    ans *= 9
    used.remove(s[0])
for sym in s[1:]:
    if sym == '?':
        ans *= 10
    elif sym in used:
        ans *= len(used)
        used.remove(sym)
print(ans)
