gans = []
for _ in range(int(input())):
    p, f = list(map(int, input().split()))
    n, m = list(map(int, input().split()))
    s, w = list(map(int, input().split()))
    if s > w:
        s, w = w, s
        n, m = m, n
    ans = 0
    for i in range(min(n, p // s) + 1):
        j = min(n - i, f // s)
        p1 = p - i * s
        f1 = f - j * s
        ansi = i + j + min(f1 // w + p1 // w, m)
        ans = max(ans, ansi)
    gans.append(ans)
print('\n'.join(map(str, gans)))

