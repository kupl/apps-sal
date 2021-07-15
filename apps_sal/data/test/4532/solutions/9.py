def solve():
    n, k = list(map(int, input().split()))
    a = [int(x) for x in input().split()]
    used = {}
    ans = 0
    for i in a:
        if i % k != 0:
            if (i % k) in used:
                ans = max(ans, k * (used[i % k] + 1) - (i % k))
                used[i % k] += 1
            else:
                ans = max(ans, k - (i % k))
                used[i % k] = 1
    print(ans if ans == 0 else ans + 1)


[solve() for i in range(int(input()))]

