S = input()

a = S.count('a')
ls = (len(S) - a) // 2 + a

s1 = S[:ls]
s2 = S[ls:]

if (len(S) - a) % 2 != 0 or 'a' in s2:
    print(":(")
else:
    f = []
    for t in s1:
        if t != 'a':
            f += [t]
    if f != list(s2):
        print(":(")
    else:
        print(s1)
