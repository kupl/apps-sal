for _ in range(int(input())):
    n, k, d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = {}
    for q in range(d):
        s[a[q]] = s.get(a[q], 0) + 1
    ans = len(s)
    for q in range(d, n):
        if s[a[q - d]] == 1:
            del s[a[q - d]]
        else:
            s[a[q - d]] -= 1
        s[a[q]] = s.get(a[q], 0) + 1
        ans = min(ans, len(s))
    print(ans)
