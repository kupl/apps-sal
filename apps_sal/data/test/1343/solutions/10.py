def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m] < t:
            min = m + 1
        elif seq[m] > t:
            max = m - 1
        else:
            return m


n, m, k = [int(i) for i in input().split()]
s = [[] for i in range(n)]
for i in range(m):
    u, v, l = [int(i) for i in input().split()]
    s[u - 1].append([v - 1, l])
    s[v - 1].append([u - 1, l])
if k == 0 or k == n:
    print(-1)
else:
    o = [int(i) - 1 for i in input().split()]
    o.sort()
    a = 10**9 + 1
    for i in o:
        for j in s[i]:
            if binary_search(o, j[0]) == -1:
                a = min(j[1], a)
    if a == 10**9 + 1:
        print(-1)
    else:
        print(a)
