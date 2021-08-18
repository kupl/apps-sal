import itertools
H, W = map(int, input().split())
A = []
for _ in range(H):
    a = list(input())
    if a.count("
        A.append(a)

H=len(A)
if H == 1:
    A=list(itertools.chain.from_iterable(A))
    cnt=[]
    for ans in A:
        if ans == "
            cnt.append(ans)
    print("".join(cnt))
else:
    L=[]
    for w in range(W):
        l=[]
        for h in range(H):
            if A[h][w] == "
                l=[]
                break
            l.append(w)
        if len(l) != 0:
            L.append(l[0])

    def dellist(items, indexes): return [item for index, item in enumerate(items) if index not in indexes]
    for ans in A:
        ans=dellist(ans, L)
        print("".join(ans))
