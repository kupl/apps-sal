def solve(n, k):
    s = list(map(int, input().split()))
    s.sort()
    ans = 0
    p = s[0]
    for i in range(1, n):
        ans += (k - s[i]) // p
    print(ans)


for _ in range(int(input())):
    (n, k) = map(int, input().split())
    solve(n, k)
