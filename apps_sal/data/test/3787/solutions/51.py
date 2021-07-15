N,A,B = map(int,input().split())
if A+B-1>N or N>A*B:
    print(-1)
else:
    G = {i:[] for i in range(1,A+1)}
    i = A
    cnt = 0
    cur = N
    while cur>A:
        G[i].append(cur)
        cnt += 1
        cur -= 1
        if cnt==B-1:
            cnt = 0
            i -= 1
    C = []
    for i in range(1,A+1):
        C += G[i]
        C.append(i)
    print(*C)
