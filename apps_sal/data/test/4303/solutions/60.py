(n, k) = list(map(int, input().split()))
xl = list(map(int, input().split()))
if 0 in xl:
    k -= 1
else:
    xl.append(0)
    xl.sort()
if k == 0:
    ans = 0
else:
    ans = 10 ** 9
    zeropoint = xl.index(0)
    endpoint = len(xl) - 1
    startpoint = max(0, zeropoint - k)
    cur = startpoint
    while cur + k <= endpoint and cur <= zeropoint:
        if cur < zeropoint < cur + k:
            tempdis = abs(xl[cur] - xl[cur + k])
            tempdis += min(abs(xl[cur]), xl[cur + k])
            ans = min(ans, tempdis)
        else:
            ans = min(ans, abs(xl[cur] - xl[cur + k]))
        cur += 1
print(ans)
