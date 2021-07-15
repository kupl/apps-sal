N, M = list(map(int, input().split()))
st = 1 * 10 ** (N-1)
en = st * 10
SC = []
for i in range(M):
    sc = list(map(int,input().split()))
    SC.append(sc)
if N == 1:
    for i in range(0, 10):
        t = str(i)
        judge = True
        for j in range(M):
            if t[SC[j][0] - 1] != str(SC[j][1]):
                judge = False
        if judge:
            print(i)
            return
    print("-1")
    return
    
for i in range(st,en):
    t = str(i)
    judge = True
    for j in range(M):
        if t[SC[j][0]-1] != str(SC[j][1]):
            judge = False
    if judge:
        print(i)
        return
print("-1")

