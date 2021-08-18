def read(): return map(int, input().split())


n, m, k = read()
a = sorted(read())
s = sum(a)
if m <= k:
    print(0)
elif k + s - n < m:
    print(-1)
else:
    t = k
    result = 0
    for i in range(n - 1, -1, -1):
        t += a[i] - 1
        result += 1
        if t >= m:
            break
    print(result)
