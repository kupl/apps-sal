def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = [0] * (n + 1)
    for i in a:
        c[i] += 1
    ans = 0
    for tw in range(1, 101):
        cans = 0
        b = [0] * (n + 1)
        for i in a:
            j = tw - i
            if j > n or j <= 0:
                continue
            if i != j and c[i] - b[i] >= 1 and c[j] - b[j] >= 1 \
                    or i == j and c[i] - b[i] >= 2:
                b[i] += 1
                b[j] += 1
                cans += 1
        ans = max(ans, cans)
    print(ans)


t = int(input())
for _ in range(t):
    solve()
