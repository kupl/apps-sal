n = int(input())
s = list(map(int, input().split()))
ans = 0
for d in range(1, n - 1):
    ten = 0
    passed = set([0, n - 1])
    l = 0
    r = n - 1
    for _ in range((n - 1) // d):
        l += d
        r -= d
        if l in passed or r in passed or l == r or r < d:
            break
        ten += s[l]
        ten += s[r]
        passed.add(l)
        passed.add(r)
        if ten > ans:
            ans = ten
print(ans)
