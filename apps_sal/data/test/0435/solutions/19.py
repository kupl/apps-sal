def solve(k, s, c):
    p = [-1, len(s)]
    for i in range(len(s)):
        if s[i] == c:
            p += [i]
    p.sort()
    n = len(p)
    if n - k - 1 <= 0:
        return len(s)
    m = 0
    for i in range(n - k - 1):
        m = max(m, p[i + k + 1] - p[i])
    return m - 1


n, k = list(map(int, input().split()))
s = input()

print(max(solve(k, s, 'a'), solve(k, s, 'b')))
