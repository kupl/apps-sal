def solve(a, b, c):
    ans = 0
    for da in range(max(0, b + c - a), l + 1):
        x = min(a - b - c + da, l - da)
        ans += (x + 1) * (x + 2) // 2
    return ans


a, b, c, l = list(map(int, input().split()))
print((l + 1) * (l + 2) * (l + 3) // 6 - solve(a, b, c) - solve(b, a, c) - solve(c, a, b))
