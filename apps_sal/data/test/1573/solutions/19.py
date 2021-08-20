def key_tri(argument):
    return argument[0]


(n, d) = list(map(int, input().split()))
L = [list(map(int, input().split())) for _ in range(n)]
L.sort(key=key_tri)
deb = 0
T = []
s = 0
for k in range(1, n):
    if L[k][0] - L[deb][0] >= d:
        s = 0
        for i in range(deb, k):
            s += L[i][1]
        T += [s]
        s = deb + 1
        while L[k][0] - L[s][0] >= d:
            s += 1
        deb = s
s = 0
for k in range(deb, n):
    s += L[k][1]
T = T + [s]
print(max(T))
