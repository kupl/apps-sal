t = int(input())
for i in range(t):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = k
    s = dict()
    c = 0
    for j in range(d):
        if a[j] in s:
            s[a[j]] += 1
        else:
            c += 1
            s[a[j]] = 1
    mm = m = len(s)
    for j in range(d, n):
        if a[j-d] in s:
            s[a[j-d]] -= 1
            if s[a[j-d]] == 0:
                del s[a[j-d]]
                m -= 1
        else:
            s[a[j]] = 1
            m += 1
        if a[j] in s:
            s[a[j]] += 1
        else:
            s[a[j]] = 1
            m += 1
        if m < mm:
            mm = m
    print(mm)




