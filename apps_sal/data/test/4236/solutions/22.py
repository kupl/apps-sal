t = 1
for test in range(1, t + 1):
    (n, m) = list(map(int, input().split()))
    ans = []
    count = 0
    D = {}
    for i in range(n):
        (l, r) = list(map(int, input().split()))
        for j in range(l, r + 1):
            D[j] = 1
    for i in range(1, m + 1):
        if i not in D:
            count += 1
            ans.append(i)
    print(count)
    print(*ans)
