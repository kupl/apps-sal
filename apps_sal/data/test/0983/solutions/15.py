n, p, q, r = map(int, input().split())
list1 = list(map(int, input().split()))
pref = [list1[0]]
suf = [list1[-1]]
ans = -3 * 10 ** 18 - 1
if p > 0:
    for i in range(1, n):
        pref.append(max(list1[i], pref[-1]))
else:
    for i in range(1, n):
        pref.append(min(list1[i], pref[-1]))
if r > 0:
    for i in range(n - 2, -1, -1):
        suf.append(max(suf[-1], list1[i]))
else:
    for i in range(n - 2, -1, -1):
        suf.append(min(suf[-1], list1[i]))
for i in range(n):
    ans = max(ans, pref[i] * p + q * list1[i] + suf[n - i - 1] * r)
print(ans)
