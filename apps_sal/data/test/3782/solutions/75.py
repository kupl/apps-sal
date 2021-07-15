from heapq import heappop,heappush

n,k,q = map(int,input().split())
a = list(map(int,input().split()))

if(q==1):
    print(0)
    return()

ans = max(a)
rem = [0] * n
while(True):
    nums = [[]]
    i = 0
    while(i<n):
        if(rem[i]==0):
            heappush(nums[-1],a[i])
        else:
            if(nums[-1]):
                nums.append([])
        i += 1

    mins = []
    for hq in nums:
        while(len(hq) >= k):
            mins.append( heappop(hq) )

    if(len(mins) < q):
        print(ans)
        return()

    mins.sort()
    y = mins[0]
    x = mins[q-1]
    ans = min(ans, x-y)
    for i,ai in enumerate(a):
        if(ai==y):
            rem[i] = 1
