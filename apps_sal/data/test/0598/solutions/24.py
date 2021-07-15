f = lambda: list(map(int, input().split()))
n, x = f()
s = [[] for i in range(x - 1)]
for d in range(n):
    l, r, c = f()
    if r - l < x - 1: s[r - l].append((l, c))
for t in s: t.sort(key=lambda q: q[0])
m = 3e9
for d, t in enumerate(s):
    D = x - 2 - d
    i, T = 0, s[D]
    M = 3e9
    for l, c in t:
        while i < len(T) and l > T[i][0] + D:
            M = min(M, T[i][1])
            i += 1
        m = min(m, c + M)
print(-1 if m == 3e9 else m)




# Made By Mostafa_Khaled

