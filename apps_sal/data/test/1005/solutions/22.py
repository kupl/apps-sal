t = int(input())
for i in range(t):
    (n, k, d) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = dict()
    for i in range(n):
        b[a[i]] = 0
    count = 0
    for i in range(d):
        if b[a[i]] == 0:
            count += 1
        b[a[i]] += 1
    ans = count
    for i in range(n - d):
        if b[a[i]] == 1:
            count -= 1
        b[a[i]] -= 1
        if b[a[i + d]] == 0:
            count += 1
        b[a[i + d]] += 1
        ans = min(ans, count)
    print(ans)
