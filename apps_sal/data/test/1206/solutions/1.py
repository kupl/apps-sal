n = int(input())
L = []
for i in range(n) :
    l,r = map(int, input().split(' '))
    L.append([l,r])
for i in range(n, 5) :
    L.append([0,0])
ans = 0.0
for s in range(1, 10001) :
    P = [0]*5
    for i in range(5) :
        P[i] = max(min((L[i][1] - s+1)/(L[i][1]-L[i][0]+1), 1.0), 0.0)
    P0 = 1.0
    for i in range(5) :
        P0 *= (1-P[i])
    P1 = 0.0
    for i in range(5) :
        t = P[i]
        for j in range(5) :
            if i == j : continue
            t *= (1-P[j])
        P1 += t
    ans += 1.0 - P0 - P1
print(ans)
