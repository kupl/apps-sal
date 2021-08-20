(n, m) = list(map(int, input().split()))
sol = True
dst = set()
for _ in range(n):
    l = input()
    g = s = 0
    for j in range(m):
        if l[j] == 'G':
            g = j
        if l[j] == 'S':
            s = j
    if s < g:
        sol = False
    else:
        dst.add(g - s)
print(len(dst) if sol else -1)
