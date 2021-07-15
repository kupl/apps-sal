N = int(input())
P = list(map(int, input().split()))
R = list(range(N))
L = list(range(N))
I = [-1] * (N+1)
for i, p in enumerate(P):
    I[p] = i

ans = 0
for n, idx in enumerate(I[1:], 1):
    #print(f"n={n}, idx={idx}")
    l = idx-1
    while l>=0 and l!=L[l]:
        l = L[l]
    r = idx+1
    while r<N and r!=R[r]:
        r = R[r]
    L[idx] = l
    R[idx] = r

    if l != -1:
        l2 = l-1
        while l2>=0 and l2!=L[l2]:
            l2 = L[l2]
        #print(f"n * (l-l2) * (r-idx) = {n * (l-l2) * (r-idx)}")
        #print(l, l2)
        ans += n * (l-l2) * (r-idx)
        #L[l] = l2
    if r != N:
        r2 = r+1
        while r2<N and r2!=R[r2]:
            r2 = R[r2]
        #print(f"n * (idx-l) * (r2-r) = {n * (idx-l) * (r2-r)}")
        ans += n * (idx-l) * (r2-r)
        #R[r] = r2
print(ans)

