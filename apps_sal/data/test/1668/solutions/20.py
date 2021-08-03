def withZeros(m):
    t = str(m)
    if m < 1000:
        t = "0" + t
        if m < 100:
            t = "0" + t
            if m < 10:
                t = "0" + t
    return t


q = int(input())
for query in range(q):
    n = int(input())
    r = [0 for i in range(n)]
    for i in range(n):
        r[i] = int(input())
    w = [r[i] % 1000 for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if r[i] == r[j]:
                ans += 1
                for a in range(10):
                    if ((r[i] + a * 1000 + 1000) % 10000) not in r:
                        r[i] = (r[i] + a * 1000 + 1000) % 10000
                        break
    print(ans)
    for i in range(n):
        print(withZeros(r[i]))
