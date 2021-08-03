n, k, l = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
i = 1
m = k * n
if(a[n - 1] - a[0] > l):
    print(0)
else:
    while(i < m and a[i] <= a[0] + l):
        i += 1
    if(i == m or m - i + 1 < k):
        ans = 0
        for j in range(0, m, k):
            ans += a[j]
        print(ans)
    else:
        usables = m - i - k + 1
        ind = i - 1
        ans = 0
        while(ind >= 0):
            ans += a[ind]
            if(usables >= k - 1):
                usables -= k - 1
                ind -= 1
            elif(usables > 0):
                ind -= (k - usables)
                usables = 0
            else:
                ind -= k
        print(ans)
