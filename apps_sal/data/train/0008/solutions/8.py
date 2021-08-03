def solve():
    n, k = list(map(int, input().split()))
    s = input()
    ans = 0
    prev = False
    c = []
    cc = 0
    for i in range(n):
        if s[i] == 'W':
            if cc:
                if cc != i:
                    c.append(cc)
                cc = 0
            if prev:
                ans += 2
            else:
                ans += 1
            prev = True
        else:
            prev = False
            cc += 1
    c.sort()
    for i in range(len(c)):
        if c[i] <= k:
            k -= c[i]
            ans += c[i] * 2 + 1
    if 'W' in s:
        ans += k * 2
    else:
        ans += max(k * 2 - 1, 0)
    ans = min(ans, n * 2 - 1)
    print(ans)


t = int(input())
for _ in range(t):
    solve()
