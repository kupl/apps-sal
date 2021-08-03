def resolve():
    n = int(input())
    h = tuple(map(int, input().split()))
    ans = 0
    r = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            r += 1
        else:
            ans = max(ans, r)
            r = 0
    ans = max(ans, r)
    print(ans)


resolve()
