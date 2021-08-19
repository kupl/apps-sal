tc = int(input())
for i in range(tc):
    ans = 0
    (a, b, c, d) = list(map(int, input().split()))
    for j in range(a, b + 1):
        if j < c and j < d:
            ans += d - c + 1
        if j >= c and j < d:
            ans += d - j
        if j > d:
            break
    print(ans)
