for _ in range(int(input())):
    _, _, n = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    cnt = dict()
    for i in a[:n]:
        cnt[i] = cnt.get(i, 0) + 1
    mlen = len(cnt)
    for i in range(n, len(a)):
        if a[i - n] != a[i]:
            if cnt[a[i - n]] == 1:
                del cnt[a[i - n]]
            else:
                cnt[a[i - n]] -= 1
            cnt[a[i]] = cnt.get(a[i], 0) + 1
            mlen = min(mlen, len(cnt))
    print(mlen)
