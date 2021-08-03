N, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))

done = [-1] * N
done[0] = 0

tmp = 0
done[0] = 0
for k in range(1, K + 1):
    tmp = A[tmp]
    if done[tmp] >= 0:
        for _ in range((K - done[tmp]) % (k - done[tmp])):
            tmp = A[tmp]
        print(tmp + 1)
        return
    else:
        done[tmp] = k
print(tmp + 1)
