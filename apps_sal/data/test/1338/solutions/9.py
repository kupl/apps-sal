n, m = map(int, input().split())
s = 1
c = n - 1
arr = [0] * n
i = 0
while i <= c:
    r = 0
    j = s
    while j <= n and r < m:
        if j < n:
            r += 2 ** (n - j - 1)
        j += 1
    #print(s, j, r, m)
    if j > s and j != n + 1:
        r -= 2 ** (n - j)
    m -= r
    j -= 1
    arr[i] = j
    while s < j:
        arr[c] = s
        c -= 1
        s += 1
    s += 1
    i += 1
for i in arr:
    print(i, end=' ')
