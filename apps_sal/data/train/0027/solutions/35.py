t = int(input())
for i in range(t):
    ans = 0
    n = int(input())
    a = list(map(int, input().split()))
    for j in range(n):
        count = 0
        while a[j] % 2 == 0:
            a[j] = a[j] // 2
            count += 1
        a[j] = [a[j], count]
    a.sort()
    j = 0
    while j != n:
        m = a[j][1]
        while j + 1 < n and a[j][0] == a[j + 1][0]:
            m = max([a[j][1], a[j + 1][1]])
            j += 1
        j += 1
        ans += m
    print(ans)
