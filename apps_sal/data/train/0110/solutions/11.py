t = int(input())
for ii in range(t):
    (n, k) = map(int, input().split())
    a = list(map(int, input().split()))
    p = [0] * n
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            p[i] = 1
    cur = 0
    ind = k - 1
    for i in range(k):
        if i != 0 and i != k - 1:
            cur += p[i]
    ans = cur
    ans_ind = k - 1
    while ind < n:
        if p[ind - k + 2]:
            cur -= 1
        if p[ind]:
            cur += 1
        if cur > ans:
            ans = cur
            ans_ind = ind + 1
        ind += 1
    print(ans + 1, ans_ind - k + 2)
