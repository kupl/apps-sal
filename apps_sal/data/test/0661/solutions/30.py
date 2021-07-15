M, K = (int(i) for i in input().split())

if M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print("-1")
else:
    N = 2**M
    if K >= N:
        print("-1")
    elif K == 0:
        l = list(range(N))
        ll = l + l[::-1]
        ll = [str(a) for a in ll]
        print(" ".join(ll))
    else:
        l = list(range(N))
        l = l[:K] + l[K+1:]
        ll = [0, K] + l + [K] + l[::-1][:-1]
        ll = [str(a) for a in ll]
        print(" ".join(ll))   
