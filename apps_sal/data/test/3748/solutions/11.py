h,w = map(int,input().split())
s = [input() for _ in range(h)]
a = [-1]*h
b = [1]*w

def check(x):
    if x==0:
        return 1
    i = b.index(1)
    if x&1:
        if all(s[p][i] == s[a[p]][i] for p in range(h)):
            b[i] = 0
            if check(x-1): return 1
            b[i] = 1
    for j in range(i+1,w):
        if b[j] and all(s[p][i] == s[a[p]][j] for p in range(h)):
            b[i] = b[j] = 0
            if check(x-2): return 1
            b[i] = b[j] = 1
    return 0

def dfs(x):
    if x==0:
        return check(w)
    i = a.index(-1)
    if x&1:
        a[i] = i
        if dfs(x-1): return 1
        a[i] = -1
    for j in range(i+1,h):
        if a[j] == -1:
            a[i],a[j] = j,i
            if dfs(x-2): return 1
            a[i] = a[j] = -1
    return 0

print("YES" if dfs(h) else "NO")
