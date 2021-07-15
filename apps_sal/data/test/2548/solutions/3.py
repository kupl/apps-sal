from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i] - 1
    t = defaultdict(int)
    t[s[0]] += 1
    ans = 0
    for i in range(1, n + 1):
        ans += t[s[i]]
        t[s[i]] += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
