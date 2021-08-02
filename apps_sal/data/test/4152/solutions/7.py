from bisect import bisect_right as bs
n = int(input())
s = list(map(int, input().split()))
s.sort()
d = dict()
for i in range(n):
    try:
        d[s[i]] += 1
    except:
        d.update({s[i]: 1})
ans = 0
d1 = dict()
for i in range(n - 1, -1, -1):
    x = len(bin(s[i])) - 2
    y = 2**x
    dif = abs(y - s[i])
    ind = bs(s, dif)
    if s[ind - 1] == dif:
        if s[ind - 1] == s[i] and d[s[i]] == 1:
            True
        else:
            d1.update({s[i]: 1})
            d1.update({s[ind - 1]: 1})

for i in range(n):
    try:
        d1[s[i]]
    except:
        ans += 1
print(ans)
