N, M = map(int, input().split())
ab = []
for _ in range(N):
    ab.append(list(map(int, input().split())))
cd = []
for _ in range(M):
    cd.append(list(map(int, input().split())))
    
for x in ab:
    a = x[0]
    b = x[1]
    cnt = []
    for y in cd:
        c = y[0]
        d = y[1]
        k = abs(a-c)+abs(b-d)
        cnt.append(k)
    print(cnt.index(min(cnt))+1)
