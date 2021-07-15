n, t, c = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
pref = [0]
for i in range(n):
    if a[i] > t:
        pref.append(pref[-1] + 1)
    else:
        pref.append(pref[-1])
cnt = 0
for i in range(n - c + 1):
    if pref[i] == pref[i + c]:
        cnt += 1
print(cnt)
