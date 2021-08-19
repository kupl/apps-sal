def rd():
    return list(map(int, input().split()))


(n, k) = rd()
a = rd()
p = [0] * 12
sz = [0] * (n + 5)
p[0] = 1
r = [{} for _ in range(11)]
for i in range(1, 11):
    p[i] = 10 % k * p[i - 1] % k
for i in range(n):
    tmp = a[i]
    ct = len(str(a[i]))
    sz[i] = ct
    if a[i] % k not in r[ct]:
        r[ct][a[i] % k] = 1
    else:
        r[ct][a[i] % k] += 1
ans = 0
for i in range(n):
    rm = a[i] % k
    for j in range(1, 11):
        req = (k - rm * p[j] % k) % k
        if req in r[j]:
            ans += r[j][req]
        if req == rm and sz[i] == j:
            ans -= 1
print(ans)
