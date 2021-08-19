n = int(input())
mod = 998244353
ans = 0
arr = list(map(int, input().split(' ')))
counti = [0] * 11
maxi = -1
for i in range(n):
    val = len(str(arr[i]))
    counti[val] += 1
    maxi = max(maxi, val)
for i in range(n):
    x = arr[i]
    curr = str(x)
    currl = len(curr)
    for f in range(1, maxi + 1):
        currc = counti[f]
        req1 = curr[0]
        if currc == 0:
            continue
        if f >= currl:
            tmp = 0
            for j in range(1, len(curr)):
                req1 += '0'
                req1 += curr[j]
            req2 = req1 + '0'
        else:
            posl = currl - f
            req1 = ''
            for j in range(0, posl):
                req1 += curr[j]
            req2 = req1
            req1 += curr[posl]
            for j in range(posl + 1, len(curr)):
                req1 += '0'
                req1 += curr[j]
            req1 += '0'
            for j in range(posl, len(curr)):
                req2 += '0'
                req2 += curr[j]
        v1 = int(req2)
        v2 = int(req1)
        v1 = v1 % mod * (currc % mod) % mod
        v2 = v2 % mod * (currc % mod) % mod
        ans = (ans % mod + v1 % mod) % mod
        ans = (ans % mod + v2 % mod) % mod
print(ans)
