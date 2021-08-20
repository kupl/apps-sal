(n, m) = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(m)]
D1 = [0 for _ in range(n)]
D2 = [0 for _ in range(n)]
for i in range(m):
    s = S[i]
    a = max(s)
    b = min(s)
    D1[a - 1] += 1
    D2[b - 1] += 1
ok = 1
a1 = -1
a2 = -1
for i in range(n):
    if D1[i] and D2[i]:
        ok = 0
    if D1[i] and a1 < 0:
        a1 = i
    if D2[i]:
        a2 = i
if a1 < a2:
    ok = 0
if ok:
    r = 1
    G = []
    b = a1
    if b == -1:
        b = n + 1
    for i in range(n):
        if D1[i] == 0 and D2[i] == 0:
            if i >= a2 and i <= b:
                r += 1
    if a1 == -1:
        r -= 1
    if a2 == -1:
        r -= 1
    print(r)
else:
    print(0)
