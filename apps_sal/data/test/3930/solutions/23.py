n, k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

psum = [0]
d = {0: 1}
for i in range(n):
    num = psum[i] + arr[i]
    d.setdefault(num, 0)
    d[num] += 1
    psum.append(num)

if abs(k) == 1:
    e = d.copy()
    ans = 0
    for i in psum:
        e[i] -= 1
        if 1 + i in e: ans += e[1 + i]

    if k == -1:
        e = d.copy()
        for i in psum:
            e[i] -= 1
            if i - 1 in e: ans += e[i - 1]

    print(ans)


else:
    p = 0
    w = pow(k, p)
    ans = 0
    while w <= pow(10, 14):
        e = d.copy()

        for i in psum:
            e[i] -= 1
            if w + i in e: ans += e[w + i]

        p += 1
        w = pow(k, p)

    print(ans)
