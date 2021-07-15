n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d1 = {a[0] : 1}
d2 = {}
dp1 = [0]
dp2 = [0, 0]
for i in range(1, n):
    if a[i] % k == 0 and a[i] // k in d1:
            dp1.append(d1[a[i] // k])
            if a[i] % (k ** 2) == 0 and a[i] // k in d2:
                #dp2.append(sum(d2[a[i] // k]))
                dp2.append(d2[a[i] // k])
            else:
                dp2.append(0)
    else:
        dp1.append(0)
        dp2.append(0)
    if a[i] in d1:
        d1[a[i]] += 1
    else:
        d1[a[i]] = 1
    if a[i] in d2:
        d2[a[i]] += dp1[i]
    else:
        d2[a[i]] = dp1[i]

print(sum(dp2))

