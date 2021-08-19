string_ = input()
(s, b) = string_.split()
s = int(s)
b = int(b)
string_ = input()
arr = string_.split()
arr = [int(x) for x in arr]
base = []
for i in range(b):
    string_ = input()
    (d, g) = string_.split()
    d = int(d)
    g = int(g)
    base.append((d, g))
base.sort()
pref = []
for i in range(b):
    if i == 0:
        pref.append(base[i][1])
    else:
        pref.append(pref[i - 1] + base[i][1])
for i in range(s):
    ans = 0
    (lef, r) = (0, b)
    while r - lef > 1:
        mid = int((r + lef) / 2)
        if base[mid][0] > arr[i]:
            r = mid
        else:
            lef = mid
    if lef == 0:
        if base[lef][0] <= arr[i]:
            ans += pref[lef]
    else:
        ans += pref[lef]
    print(ans, end=' ')
