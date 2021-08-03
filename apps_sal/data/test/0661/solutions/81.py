M, K = map(int, input().split())
if M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
elif K >= 2**M:
    print(-1)
else:
    ls = list(range(2**M))
    ls.remove(K)
    ans = [K] + ls + [K] + ls[::-1]
    print(' '.join(map(str, ans)))
