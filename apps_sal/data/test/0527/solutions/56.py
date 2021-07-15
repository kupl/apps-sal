from bisect import bisect_right
s = input()
t = input()

n = len(s)

if set(list(t)) != (set(list(s)) & set(list(t))): ans = -1
else:
    dct = {}

    for i, ss in enumerate(s):
        if ss in dct:
            dct[ss].append(i)
        else: dct[ss] = [i]
    idx = -1
    ans = 0
    for tt in t:
        m = bisect_right(dct[tt], idx)
        if m == len(dct[tt]):
            idx = dct[tt][0]
            ans += n
        else:
            idx = dct[tt][m]
    ans += idx + 1

print(ans)
