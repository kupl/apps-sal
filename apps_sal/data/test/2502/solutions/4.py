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
d = [-1] * (len(s)+1) 
for a, b in kmp_search(m*s, t):
    a, b = a%len(s)+1, b%len(s)+1
    d[a] = b


ls = [-1]*(len(s)+1)
vs = set()
for i in range(1, len(s)+1):
    if i in vs:
        continue
    c = 0
    j = i
    while True:
        vs.add(i)
        i = d[i]
        if i == -1:
            break
        c += 1
        if i == j:
            c = inf
            break
        if ls[i] != -1:
            c += ls[i]
            break
    if c == inf:
        break
    ls[j] = c
print((max(ls) if c != inf else -1))

