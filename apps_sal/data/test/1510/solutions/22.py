(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_min = min(a)
b_max = max(b)
if a_min >= b_max:
    print(0)
else:
    a = sorted([i for i in a if i < b_max])
    n = len(a)
    aa = [0] * (n + 1)
    for i in range(n):
        aa[i + 1] = aa[i] + a[i]
    b = sorted([i for i in b if i > a_min])
    m = len(b)
    bb = [0] * (m + 1)
    for i in range(m - 1, -1, -1):
        bb[i] = bb[i + 1] + b[i]
    output = float('inf')
    i = 0
    j = 0
    while i < n or j < m:
        if i == n:
            k = b[j]
        elif j == m:
            k = a[i]
        else:
            k = min(a[i], b[j])
        while i < n and a[i] <= k:
            i += 1
        while j < m and b[j] <= k:
            j += 1
        output = min(output, k * (i - m + j) - aa[i] + bb[j])
    print(int(output))
