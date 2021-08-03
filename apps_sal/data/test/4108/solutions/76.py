S, T = input(), input()

d = [None] * 26
flag = True
for s, t in zip(S, T):
    s = ord(s) - ord('a')
    t = ord(t) - ord('a')
    if d[s] is None:
        d[s] = t
    elif d[s] != t:
        flag = False
        break

if not flag:
    print('No')
elif len(set(v for v in d if v is not None)) != sum(int(v is not None) for v in d):
    print('No')
else:
    print('Yes')
