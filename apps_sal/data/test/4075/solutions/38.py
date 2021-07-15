n, m = map(int, input().split(' '))
K = []
S = []
for i in range(m):
    l = list(map(int, input().split(' ')))
    K.append(l[0])
    S.append(l[1:])
p = list(map(int, input().split(' ')))
ans = 0
for i in range(2**n):
    light = 0
    for j in range(m):
        sw = 0
        for s in S[j]:
            if (i>>(s-1))&1:
                sw += 1
        if sw%2 == p[j]:
            light+=1
    if light == m:
        ans += 1
print(ans)
