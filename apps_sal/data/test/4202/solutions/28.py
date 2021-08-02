l, r = map(int, input().split())

if r - l >= 2019:
    print(0)
else:
    ans = float("inf")
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            t = i * j % 2019
            if t < ans:
                ans = t
    print(ans)
