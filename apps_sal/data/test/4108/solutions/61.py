S = input()
T = input()

D1 = {}
D2 = {}

ans = 1
for s, t in zip(S, T):
    x = D1.get(t, '')
    if x == '':
        D1[t] = s
    else:
        if x != s:
            ans = 0
            break

    x = D2.get(s, '')
    if x == '':
        D2[s] = t
    else:
        if x != t:
            ans = 0
            break

print('Yes' if ans else 'No')
