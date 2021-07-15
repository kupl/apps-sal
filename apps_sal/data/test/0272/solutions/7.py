s1 = input()
s2 = input()
d = dict()
for i in range(len(s1)):
    if s2[i] != s1[i]:
        res1 = d.get(s1[i], -1)
        res2 = d.get(s2[i], -1)
        if (res1 == -1 and res2 == -1) or (res1 == s2[i] and res2 == s1[i]):
            d[s1[i]] = s2[i]
            d[s2[i]] = s1[i]
        else:
            print(-1)
            return
    if s2[i] == s1[i]:
        res = d.get(s1[i], -1)
        if res != -1 and res != s1[i]:
            print(-1)
            return
        d[s1[i]] = s1[i]
ans = len(d)
for i in d:
    if i == d[i]:
        ans -= 1
print(ans // 2)
used = dict()
for i in d:
    used[i] = 0
for i in d:
    if not used[i] and i != d[i]:    
        print(i, d[i])
        used[d[i]] = 1
