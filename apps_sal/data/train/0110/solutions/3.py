t = int(input())
for qq in range(t):
    n, k = list(map(int, input().split()))
    m = list(map(int, input().split()))
    p = 0
    for i in range(n - k + 1, n - 1):
        if m[i] > m[i - 1] and m[i] > m[i + 1]:
            p += 1
    mp = p
    ii = n - k + 1
    for i in range(n - k, 0, -1):
        if m[i] > m[i - 1] and m[i] > m[i + 1]:
            p += 1
        if m[i + k - 2] > m[i + k - 3] and m[i + k - 2] > m[i + k - 1]:
            p -= 1
        if p >= mp:
            mp = p
            ii = i
    print(mp + 1, ii)
