n, K = list(map(int, input().split()))
A = list([int(x) - 1 for x in input().split()])
done = [-1 for _ in range(n)]
tmp = 0
done[0] = 0
for k in range(1, K + 1):
    tmp = A[tmp]
    if done[tmp] >= 0:
        for i in range((K - done[tmp]) % (k - done[tmp])):
            tmp = A[tmp]
        print((tmp + 1))
        return
    else:
        done[tmp] = k
print((tmp + 1))

