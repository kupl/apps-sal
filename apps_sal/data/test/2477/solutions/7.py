N, K = list(map(int, input().split()))
logs = list(map(int, input().split()))
maxL = max(logs)


def binsearch(minz, maxz):
    if minz >= maxz:
        return minz

    mid = (maxz + minz) // 2
    ncut = 0
    for i in range(N):
        thiscut = int((logs[i] + mid - 1) / mid) - 1
        ncut += thiscut
        if ncut > K:
            return binsearch(mid + 1, maxz)

    if ncut < K:
        return binsearch(minz, mid)
    # else ncut == K
    maxx = 0
    for i in range(N):
        thiscut = int((logs[i] + mid - 1) / mid) - 1
        thislen = int((logs[i] + thiscut) / (thiscut + 1))
        if maxx < thislen: maxx = thislen
    return maxx


if K > 0:
    ans = binsearch(1, maxL + 1)
else:
    ans = maxL
print(ans)
