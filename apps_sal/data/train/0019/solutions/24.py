t = int(input())
for i1 in range(t):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dic = {}
    r = 0
    for i in range(d):
        e = a[i]
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
            r += 1
    m = r
    for i in range(1, n - d + 1):
        e = a[i + d - 1]
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
            r += 1
        e = a[i - 1]
        if dic.get(e) > 1:
            dic[e] -= 1
        else:
            dic.pop(e)
            r -= 1
        m = min(m, r)
    print(m)
