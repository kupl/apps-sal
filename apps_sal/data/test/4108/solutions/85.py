s = input()
t = input()

sc = {}
tc = {}

for i in range(len(s)):
    if s[i] in sc:
        sc[s[i]].append(i)
    else:
        sc[s[i]] = [i]

    if t[i] in tc:
        tc[t[i]].append(i)
    else:
        tc[t[i]] = [i]

sc = list(sc.values())
tc = list(tc.values())

print("Yes" if sc == tc else "No")
