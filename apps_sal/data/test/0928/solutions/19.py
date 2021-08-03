n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0
cur = 0
r = -1

for l in range(n):
    stop = True
    if cur < k:
        while r < n - 1:
            r += 1
            cur += a[r]
            if cur >= k:
                cnt += n - r
                stop = False
                break

    elif cur > k:
        stop = False
        if r == l:
            cnt += n - r
        else:
            while r > l:
                cur -= a[r]
                r -= 1
                if cur <= k:
                    r += 1
                    cur += a[r]
                    cnt += n - r
                    break

    else:
        cnt += n - r
        stop = False

    cur -= a[l]

    if stop:
        break

print(cnt)
