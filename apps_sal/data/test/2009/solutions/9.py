from collections import deque


def BFS(a, vertex=None):
    if vertex is None:
        vertex = 1
    s = [1]*len(a)
    d = deque([vertex])
    s[vertex] = 0
    f = {vertex}
    while len(d) > 0:
        for q in a[d.popleft()]:
            if s[q]:
                d.append(q)
                f.add(q)
                s[q] = 0
    return f


def components(a):
    s = [1]*len(a)
    d, q2 = [], 1
    while q2 < len(a):
        if s[q2]:
            if len(a[q2]) == 0:
                s[q2] = 0
                d.append({q2})
            else:
                f = BFS(a, q2)
                d.append(f)
                for q in f:
                    s[q] = 0
        else:
            q2 += 1
    return d


n = int(input())
x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
a = [[0]*(n+2)]+[[0]+list(map(int, [1-int(q) for q in list(input())]))+[0] for _ in range(n)]+[[0]*(n+2)]
d = [[] for _ in range(n**2+1)]
for q in range(1, n+1):
    for q1 in range(1, n+1):
        if a[q][q1]:
            if a[q-1][q1]:
                d[(q-1)*n+q1].append((q-2)*n+q1)
            if a[q+1][q1]:
                d[(q-1)*n+q1].append(q*n+q1)
            if a[q][q1-1]:
                d[(q-1)*n+q1].append((q-1)*n+q1-1)
            if a[q][q1+1]:
                d[(q-1)*n+q1].append((q-1)*n+q1+1)
x, y = (x1-1)*n+y1, (x2-1)*n+y2
s = components(d)
comp_x, comp_y = [], []
for q in s:
    if x in q:
        comp_x = q
    if y in q:
        comp_y = q
if comp_y == comp_x:
    print(0)
else:
    ans = float('inf')
    for q in comp_x:
        for q1 in comp_y:
            x1, x2, y1, y2 = (q-1)//n+1, (q-1) % n+1, (q1-1)//n+1, (q1-1) % n+1
            ans = min((x1-y1)**2+(x2-y2)**2, ans)
    print(ans)

