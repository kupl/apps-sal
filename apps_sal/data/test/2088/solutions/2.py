n = int(input())
if n == 1:
    print(1)
else:
    adj = [[] for i in range(n+10)]
    s = input().split()
    for i in range(2,n+1):
        pi = int(s[i-2])
        adj[i].append(pi)
        adj[pi].append(i)
        
    num = 1
    curr = [1]
    nextcurr = []
    disco = [1]
    visited = {1:True}
    while num < n:
        for v in curr:
            for w in adj[v]:
                if w not in visited:
                    nextcurr.append(w)
                    visited[w] = True
                    disco.append(w)
                    num += 1
        curr = nextcurr
        nextcurr = []

    nl = {}
    nlvals = {}
    for v in disco[::-1]:
        nl[v] = max(sum(nl.get(w,0) for w in adj[v]),1)
        nlvals[nl[v]] = nlvals.get(nl[v],0)+1
    colors = {}
    leaves = nlvals[1]
    colors[1] = leaves
    for c in range(2, leaves+1):
        colors[c] = colors[c-1] + nlvals.get(c,0)

    ans = ""
    j = 1
    for i in range(1, n+1):
        while colors[j] < i:
            j += 1
        ans += str(j) + ' '
    print(ans.strip())

