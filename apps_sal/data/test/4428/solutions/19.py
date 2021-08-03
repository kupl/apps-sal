import bisect

n = int(input())
a = list(map(int, input().split(' ')))

prefs = [a[0]] * n
suffs = [a[n - 1]] * n
for i in range(1, len(a)):
    prefs[i] = prefs[i - 1] + a[i]
for i in reversed(list(range(0, len(a) - 1))):
    suffs[i] = suffs[i + 1] + a[i]

ans = 0
for i in range(len(a)):
    s = suffs[i]
    ind = bisect.bisect_left(prefs, s)
    if prefs[ind] == s and ind < i:
        ans = s
        break

print(ans)
