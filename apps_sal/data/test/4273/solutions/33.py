n = int(input())
march = ['M', 'A', 'R', 'C', 'H']
d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
for i in range(n):
    s = input()
    if s[0] in march:
        d[s[0]] = d.get(s[0], 0) + 1
ans = 0
li = []
for i in d:
    for j in d:
        for k in d:
            if i != j and j != k and (k != i) and (not set([i, j, k]) in li):
                li.append(set([i, j, k]))
                ans += d[i] * d[j] * d[k]
print(ans)
