from collections import Counter
n, k = list(map(int, input().split())); arr = list(map(int, input().split())); arr.sort(reverse=True)
absarr = [[abs(i), 1 if i > 0 else -1 if i < 0 else 0] for i in arr]; absarr.sort(reverse=True, key=lambda x: x[0])
mod = 10**9 + 7

zeroflag = True if absarr[-1][0] == 0 else False
posnegarr = Counter([i[1] for i in absarr[:k]])
pos = posnegarr[1]; neg = posnegarr[-1]

if absarr[k - 1] == 0:
    ans = 0
elif neg % 2 == 0 or n == k:
    ans = 1
    for i in absarr[:k]:
        ans *= i[0]; ans %= mod
    if n == k and neg % 2 == 1:
        ans = -ans % mod
else:
    ans = 1
    for i in absarr[:k]:
        ans *= i[0]; ans %= mod
    if pos > 0:
        if absarr[k][0] == 0:
            ans = 0
        nextpos = nextneg = 0
        tmp = k
        while tmp < n and (nextpos == 0 or nextneg == 0):
            num = absarr[tmp]
            if num[0] == 0:
                break
            elif num[1] > 0 and nextpos == 0:
                nextpos = num[0]
            elif num[1] < 0 and nextneg == 0:
                nextneg = num[0]
            tmp += 1
        backpos = backneg = 0
        tmp = k - 1
        while backpos == 0 or backneg == 0:
            num = absarr[tmp]
            if num[1] > 0 and backpos == 0:
                backpos = num[0]
            elif num[1] < 0 and backneg == 0:
                backneg = num[0]
            tmp -= 1
        if ans == 0:
            pass
        elif nextpos * backpos > nextneg * backneg:
            ans *= nextpos * pow(backneg, -1, mod); ans %= mod
        else:
            ans *= nextneg * pow(backpos, -1, mod); ans %= mod
    else:
        nextpos = 0
        tmp = k
        while tmp < n and nextpos == 0:
            num = absarr[tmp]
            if num[1] > 0:
                nextpos = num[0]
            tmp += 1
        backneg = absarr[k - 1][0]
        if nextpos != 0:
            ans *= nextpos * pow(backneg, -1, mod); ans %= mod
        elif zeroflag:
            ans = 0
        else:
            ans = 1
            for i in arr[:k]:
                ans *= i; ans %= mod

print(ans)
