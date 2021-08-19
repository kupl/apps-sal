(n, q) = list(map(int, input().split()))
a = []
ar = [0 for i in range(n + 1)]
for i in range(q):
    (l, r) = list(map(int, input().split()))
    l -= 1
    r -= 1
    a.append((l, r))
    ar[l] += 1
    ar[r + 1] += -1
plus = 0
for i in range(n):
    plus += ar[i]
    ar[i] = plus
ans = 0
for i in range(q):
    for j in range(a[i][0], a[i][1] + 1):
        ar[j] -= 1
    pref = [0]
    count = 0
    for pos in range(n):
        if ar[pos] > 0:
            count += 1
        value = 0
        if ar[pos] == 1:
            value = 1
        pref.append(value + pref[-1])
    for pos in range(q):
        if pos != i:
            ans = max(ans, count - (pref[a[pos][1] + 1] - pref[a[pos][0]]))
    for j in range(a[i][0], a[i][1] + 1):
        ar[j] += 1
print(ans)
