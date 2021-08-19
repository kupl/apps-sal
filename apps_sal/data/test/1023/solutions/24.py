import bisect
(n, m, ta, tb, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
flg = 0
result = 0
if k >= min(m, n):
    flg = 1
    print(-1)
else:
    ar = [i + ta for i in a]
    x1 = []
    result = 0
    for i in range(n):
        x1.append(bisect.bisect_left(b, ar[i]))
        if i + m - x1[i] <= k:
            print(-1)
            flg = 1
            break
        j = k - i
        if j < 0:
            break
        result = max(result, b[x1[i] + j])
if flg == 0:
    print(result + tb)
