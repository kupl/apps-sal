s = [int(x) for x in input().split()]
(n, k, ll) = (s[0], s[1], s[2])
s = [int(x) for x in input().split()]
s.sort()
if s[n - 1] - s[0] > ll:
    print(0)
else:
    x = 0
    while x < n * k and s[x] <= ll + s[0]:
        x += 1
    if x > k * (n - 1):
        q = 0
        for i in range(n):
            q += s[i * k]
        print(q)
    else:
        add = []
        left = x - n
        while left > 0:
            if left >= k - 1:
                add.append(k - 1)
                left -= k - 1
            else:
                add.append(left)
                left = 0
        add += [0 for _ in range(n)]
        diff = [add[i] + 1 for i in range(n - 1)]
        q = s[0]
        p = 0
        for i in range(n - 1):
            p += diff[i]
            q += s[p]
        print(q)
