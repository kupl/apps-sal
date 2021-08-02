n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
if (x == 0):
    ans = 0
    s = dict()
    for elem in a:
        if elem in s:
            s[elem] += 1
        else:
            s[elem] = 1
    for key in list(s.keys()):
        ans += s[key] * (s[key] - 1)
else:
    ans = 0
    s = dict()
    for elem in a:
        if elem in s:
            s[elem] += 1
        else:
            s[elem] = 1
    for key in list(s.keys()):
        if (key ^ x) in s:
            ans += s[key] * s[key ^ x]
print(ans // 2)
