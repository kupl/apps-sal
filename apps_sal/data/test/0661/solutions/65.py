M, K = map(int, input().split())

if K>=(2**M):
    print(-1)
elif M==0:
    if K==0:
        print(0, 0)
    else:
        print(-1)
elif M==1:
    if K==0:
        print(0, 0, 1, 1)
    else:
        print(-1)
else:
    b = [str(i) for i in range(2**M) if not i==K]
    c = [str(i) for i in range(2**M-1, -1, -1) if not i==K]
    ans = b+[str(K)]+c+[str(K)]
    print(' '.join(ans))
