raw = input().split(' ')
n = int(raw[0])
k = int(raw[1])
pref = []
raw = input().split(' ')
for i in range(n):
    elem = float(raw[i])
    if len(pref) == 0:
        pref.append((elem + 1) / 2)
    else:
        pref.append(pref[-1] + (elem + 1) / 2)
best = 0
idx = k - 1
while idx < n:
    if idx == k - 1:
        best = pref[idx]
    else:
        best = max(best, pref[idx] - pref[idx - k])
    idx += 1
print(best)
