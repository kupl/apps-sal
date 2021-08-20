input = __import__('sys').stdin.readline
for _ in range(int(input())):
    (n, x) = map(int, input().split())
    s = sorted(map(int, input().split()), reverse=True)
    i = ans = 0
    c = 1
    while i < n:
        if c * s[i] >= x:
            ans += 1
            c = 1
        else:
            c += 1
        i += 1
    print(ans)
