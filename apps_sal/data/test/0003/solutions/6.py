n, q = list(map(int, input().split()))
painters = []
sections = [0] * (n + 1)
for i in range(q):
    l, r = list(map(int, input().split()))
    l -= 1
    r -= 1
    painters.append([l, r])
    sections[l] += 1
    sections[r + 1] -= 1

cnt1 = [0] * (n + 1)
cnt2 = [0] * (n + 1)
p = 0
total = 0
for i in range(n):
    p += sections[i]
    if p == 1:
        cnt1[i + 1] = cnt1[i] + 1
    else:
        cnt1[i + 1] = cnt1[i]
    if p == 2:
        cnt2[i + 1] = cnt2[i] + 1
    else:
        cnt2[i + 1] = cnt2[i]
    if p > 0:
        total += 1
ans = 0
for i in range(q - 1):
    for j in range(i + 1, q):
        [l1, r1] = painters[i]
        [l2, r2] = painters[j]
        l = max(l1, l2)
        r = min(r1, r2)
        if l <= r:
            t = total - (cnt2[r + 1] - cnt2[l]) - (cnt1[max(r1, r2) + 1] - cnt1[min(l1, l2)])
            ans = max(ans, t)
        else:
            t = total - (cnt1[r1 + 1] - cnt1[l1]) - (cnt1[r2 + 1] - cnt1[l2])
            ans = max(ans, t)
print(ans)

