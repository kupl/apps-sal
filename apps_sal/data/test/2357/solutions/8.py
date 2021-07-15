inf = 10**18
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = {}
    ans = inf
    for i in range(n):
        if a[i] in cnt:
            ans = min(ans, i - cnt[a[i]] + 1)
        cnt[a[i]] = i
    print(ans if ans != inf else -1)

