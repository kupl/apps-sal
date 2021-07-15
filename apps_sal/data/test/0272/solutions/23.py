s, t = input(), input()
fr = set()
k = dict()
l = 0
for i in range(len(s)):
    fr.add(tuple(sorted([s[i], t[i]])))
    if s[i] in k:
        if k[s[i]] != t[i]:
            print(-1)
            return
    if t[i] in k:
        if k[t[i]] != s[i]:
            print(-1)
            return
    k[t[i]] = s[i]
    k[s[i]] = t[i]
for i in fr:
    if i[0] != i[1]:
        l += 1
s1 = [i[0] for i in fr]
s2 = [i[1] for i in fr]
print(l)
for i in fr:
    if i[0] != i[1]:
        print(i[0], i[1])
