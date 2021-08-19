s = input()
l = []
for i in s:
    if i not in l:
        l.append(i)
minans = len(s) // 2 + 1
bst = -1
bfn = -1
for i in l:
    j = -1
    ans = 0
    st = s.find(i, 0)
    fn = len(s) - s[::-1].find(i, 0) - 1
    while s.find(i, j + 1) != -1:
        k = j
        j = s.find(i, j + 1)
        raz = j - k
        ans = max(ans, raz)
        ans = max(ans, max(st + 1, len(s) - fn))
    if ans < minans:
        minans = ans
print(minans)
