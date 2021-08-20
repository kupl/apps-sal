s = ''
for i in range(100000):
    s += str(i)
l = []
nn = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]
for i in range(100000):
    if i <= 9:
        l.append(i * (i + 1) // 2)
    else:
        l.append(l[-1] + i)
        for j in nn:
            if j < i:
                l[-1] += i - j
            else:
                break
q = int(input())
while q:
    lo = 0
    hi = len(l) - 1
    k = int(input())
    while hi - lo > 1:
        mi = lo + (hi - lo) // 2
        if l[mi] > k:
            hi = mi
        else:
            lo = mi
    if l[lo] == k:
        print(s[l[lo] - l[lo - 1]])
    else:
        lol = k - l[lo]
        print(s[lol])
    q -= 1
