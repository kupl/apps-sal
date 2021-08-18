for _ in range(int(input().strip())):
    n, k = map(int, input().split())
    l = [int(x) for x in input().split()]
    l.sort()
    ans = max(l[0], n - l[-1] + 1)
    for i in range(1, k):
        ans = max(((l[i] - l[i - 1]) // 2) + 1, ans)
    print(ans)
