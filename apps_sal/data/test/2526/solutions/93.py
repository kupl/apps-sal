x, y, a, b, c = list(map(int, input().split()))
p = sorted(list(map(int, input().split())))[-x:]
q = sorted(list(map(int, input().split())))[-y:]
r = sorted(list(map(int, input().split())))[::-1]

i = j = k = 0
oi = 0
while i < c:
    if x > j and y > k:
        if p[j] >= q[k] and q[k] < r[i]:
            q[k] = r[i]
            k += 1
            i += 1
        elif p[j] < q[k] and p[j] < r[i]:
            p[j] = r[i]
            j += 1
            i += 1
    elif x > j:
        if p[j] < r[i]:
            p[j] = r[i]
            j += 1
            i += 1
    elif y > k:
        if q[k] < r[i]:
            q[k] = r[i]
            k += 1
            i += 1
    if oi == i: break
    oi = i

print((sum(p) + sum(q)))
