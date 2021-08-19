n = int(input())
graph = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = int(input())
    for _ in range(a):
        (x, y) = map(int, input().split())
        graph[i][x - 1] = y
ans = 0
for p in range(2 ** n):
    q = p
    c = 0
    t = []
    l = 0
    while q:
        if q & 1:
            t.append(graph[c])
            l += 1
        q >>= 1
        c += 1
    flag = True
    for c in range(n):
        if p & 1:
            for s in t:
                if s[c] == 0:
                    flag = False
        else:
            for s in t:
                if s[c] == 1:
                    flag = False
        p >>= 1
    if flag:
        ans = max(ans, l)
print(ans)
