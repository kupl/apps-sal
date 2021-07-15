q = int(input())
for i in range(q):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = [0] * n
    for i in range(n):
        now = a[a[i] - 1]
        count = 1
        while now != a[i]:
            now = a[now - 1]
            count += 1
        ans[i] = count
    print(*ans)
