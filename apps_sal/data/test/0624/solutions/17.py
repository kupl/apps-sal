n, k, m = list(map(int, input().split()))
l = sorted(list(map(int, input().split())))
tot = 0
prefix = []
ans = 0.0
for i in range(n):
    tot += l[i]
    prefix.append(tot)
prefix.insert(0, 0)
for i in range(n + 1):
    if m > 0:
        t = prefix[n] - prefix[i]
        if i != 0:
            m -= 1
        if m <= (n - i) * k:
            t += m
        else:
            t += (n - i) * k
        if (n - i) != 0:
            t = (1.0 * t) / (n - i)
            if ans < t:
                ans = t
print("%0.20f" % ans)
