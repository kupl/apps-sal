from bisect import bisect_left
(n, l) = list(map(int, input().split()))
fl = list(map(int, input().split()))
let = list(map(int, input().split()))
pref = [0]
for i in range(n):
    pref.append(fl[i] + pref[i])
prev = 0
for l in let:
    dorm = bisect_left(pref, l, lo=prev)
    prev = dorm
    print(dorm, l - pref[dorm - 1])
