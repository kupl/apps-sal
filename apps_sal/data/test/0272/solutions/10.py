s = input()
s1 = input()
mistake = False
d = dict()
ans = []

for i in range(len(s)):
    if s[i] != s1[i]:
        if s[i] in d and s1[i] in d:
            if not (d[s[i]] == s1[i] and d[s1[i]] == s[i]):
                mistake = True
                break

        elif s[i] in d or s1[i] in d:
            mistake = True
            break
        else:
            d[s[i]] = s1[i]
            d[s1[i]] = s[i]
    else:
        if s[i] in d and d[s[i]] != s[i]:
            mistake = True
            break
        d[s[i]] = s[i]

if mistake:
    print(-1)
else:
    ans = []
    last = set()
    for elem in d:
        if elem not in last and elem != d[elem]:
            ans.append([elem, d[elem]])
        last.add(elem)
        last.add(d[elem])

    print(len(ans))
    for elem in ans:
        print(*elem)
