M, K = list(map(int, input().split()))

if K >= 2**M:
    print((-1))
elif M == 0:
    if K == 0:
        print((0,0))
    else:
        print((-1))
elif M == 1:
    if K >= 1:
        print((-1))
    else:
        print((0,0,1,1))
else:
    li = [i for i in range(2**M) if i != K]
    ans = li + [K] + list(reversed(li)) + [K]
    print((*ans))

