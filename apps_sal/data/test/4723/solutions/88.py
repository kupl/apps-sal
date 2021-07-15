S = input()
T = input()
ls = len(S)
lt = len(T)

unrestorable = 'z'*50
ans = unrestorable
for i in range(ls-lt+1):
    for j, t in enumerate(T):
        s = S[i+j]
        if s != t and s != '?':
            break
    else:
        key = (S[:i]+T+S[i+lt:]).replace('?', 'a')
        ans = min(ans, key)

print((ans if ans != unrestorable else 'UNRESTORABLE'))

