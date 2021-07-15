
for _ in range(int(input())):
    n = int(input())
    w = list(sorted(map(int, input().split())))
    ma = 0
    for s in range(2,2*n+1):
        l = 0
        r = n-1
        cnt = 0
        while l < r:
            cs = w[l] + w[r]
            if cs == s:
                cnt += 1
                l += 1
                r -= 1
            elif cs < s:
                l += 1
            else:
                r -= 1
        ma = max(cnt, ma)

    print(ma)


