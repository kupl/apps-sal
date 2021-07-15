N, K = map(int, input().split())
A = list(map(int, input().split()))
pos = 0
res = [-1] * 3*10**5
d = 0
way = []
l = 0
c = 0

for i in range(N) :
    A[i] -= 1
    
for i in range(K+1):
    if(res[pos] != -1) :
        l = d - res[pos]
        c = d - l
        res[pos] = d
        break
    res[pos] = d
    way.append(pos)
    d += 1
    pos = A[pos]

ans = 0
if(K+1 <= len(way)) :
    ans = way[K]
else :
    K -= c
    K = K%l
    ans = way[K + c]
print(ans+1)
