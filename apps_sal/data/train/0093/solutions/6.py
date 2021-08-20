import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    memo = {}
    for i in range(n):
        memo[a[i]] = i
    max_num = -1
    cnt = 0
    ans = 0
    for i in range(m):
        if max_num < memo[b[i]]:
            ans += 2 * (memo[b[i]] - cnt) + 1
            max_num = memo[b[i]]
            cnt += 1
        else:
            ans += 1
            cnt += 1
    print(ans)
