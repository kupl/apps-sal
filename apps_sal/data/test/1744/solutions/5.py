n, m = map(int, input().split())
t = list(map(int, input().split()))
tIndex = {}
tIndexSum = {}
s = 0
for i in range(n):
    r = 0
    if s + t[i] > m:
        keys = list(tIndex.keys())
        keys.sort(reverse=True)
        s1 = s
        for k in keys:
            if s1 - tIndex[k] * k + t[i] > m:
                s1 -= tIndex[k] * k
                r += tIndex[k]
            else:
                r += (s1 + t[i] - m) // k
                s1 -= ((s1 + t[i] - m) // k) * k
                if s1 + t[i] > m:
                    s1 -= k
                    r += 1
            if s1 + t[i] <= m:
                break
    print(r, end=' ')

    if not(t[i] in tIndex):
        tIndex[t[i]] = 0
    tIndex[t[i]] += 1
    if not(t[i] in tIndexSum):
        tIndexSum[t[i]] = 0
    tIndexSum[t[i]] += t[i]
    s += t[i]
# print('s=',s)
# print(tIndex)
