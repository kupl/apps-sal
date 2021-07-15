def partial_match_table(word):
    table = [0] * (len(word) + 1)
    table[0] = -1
    i, j = 0, 1
    while j < len(word):
        matched = word[i] == word[j]
        if not matched and i > 0:
            i = table[i]
        else:
            if matched:
                i += 1
            j += 1
            table[j] = i
    return table

def kmp_search(text, word):
    table = partial_match_table(word)
    i, p = 0, 0
    results = []
    while i < len(text) and p < len(word):
        if text[i] == word[p]:
            i += 1
            p += 1
            if p == len(word):
                p = table[p]
                results.append((i-len(word), i))
        elif p == 0:
            i += 1
        else:
            p = table[p]
    return results

inf = 10**18
s = input().strip()
t = input().strip()
m=(len(t)+len(s)-1+len(s)-1)//len(s)
d = set()
for a, b in kmp_search(m*s, t):
    d.add(a%len(s))

d2 = set()
for i in range(len(s)):
    if i not in d:
        d2.add(i)
q = d2

LT, LS = len(t), len(s)
dist = [inf] * LS
d = 0
while q:
    qq = []
    for x in q:
        if dist[x] == inf:
            dist[x] = d
            qq.append((x-LT)%LS)
    d += 1
    q = qq

answer = max(dist)
if answer >= inf:
    answer = -1

print(answer)

