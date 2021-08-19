def maxKSums():
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    subSum = []
    for i in range(n):
        sumd = 0
        for j in range(i, n):
            sumd += a[j]
            subSum.append(sumd)
    subSum.sort(reverse=True)
    for i in range(k):
        print(subSum[i], end=' ')


maxKSums()
