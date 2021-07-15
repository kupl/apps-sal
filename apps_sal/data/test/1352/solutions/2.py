n, x = map(int, input().split())
a = list(map(int, input().split()))
fst, last, sm = [], [], []
for i in range(1000005):
    fst.append(0)
    last.append(0)
    sm.append(0)
for i in range(n):
    if fst[a[i]] == 0:
        fst[a[i]] = i + 1
    last[a[i]] = i + 1
for i in range(x + 2):
    if fst[i] == 0:
        fst[i] = n + 1
l, ans = 0, 0
for i in range(1, x + 1):
    if fst[i] > l:
        l = max(l, last[i])
        sm[l] += 1
    else:
        break
for i in range(1, n + 1):
    sm[i] += sm[i - 1]
l, i = n + 1, x + 1
while i > 1:
    if last[i] < l:
        l = min(fst[i], l)
        ans += min(sm[l - 1] + 1, i - 1)
    else:
        break
    i -= 1
print(ans)
