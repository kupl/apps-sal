n,k = list(map(int, input().split()))
g = []
q = []
for i in range(n):
    v = input()
    p = []
    for i in v:
        p.append(i)
    v = p
    g.append(v)
    for x in range(len(v)):
        if v[x] != '.': continue
        num = 0
        if x != 0 and v[x-1] == 'S':
            num += 1
        if x+1 < len(v) and v[x+1] == 'S':
            num += 1
        q.append((num, len(g)-1, x))
q = sorted(q)
for i in range(k):
    g[q[i][1]][q[i][2]] = 'x'
an = 0
for s in g:
    for j in range(len(s)):
        if s[j] != 'S': continue
        if j != 0 and ( s[j-1] != '.' and s[j-1] != '-' ):
            an += 1
        if j+1 < len(s) and ( s[j+1] != '.' and s[j+1] != '-' ):
            an += 1
print(an)
    
for s in g:
    print("".join(s))
        

