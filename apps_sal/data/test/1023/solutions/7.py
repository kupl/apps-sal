import bisect
n, m, ta, tb, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
maxtime = 0
flag = 0
if k >= n or k >= m:
    print(-1)
else:
    for i in range(n):
        a[i] += ta
    for j in range(0, k + 1):

        x = bisect.bisect_left(b, a[j])
        if x + (k - j) >= m:
            flag = 1
            break
        else:
            maxtime = max(maxtime, b[x + (k - j)] + tb)
    if flag == 0:
        print(maxtime)
    else:
        print(-1)
