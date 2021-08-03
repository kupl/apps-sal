q = int(input())

for _ in range(q):
    ans = 10000000000
    n, m = list(map(int, input().split()))
    picture = []
    dotcount_w = []
    dotcount_h = []
    for _ in range(n):
        picture.append(input())
        dotcount_w.append(picture[-1].count("."))

    for i in range(m):
        count = 0
        for j in range(n):
            if picture[j][i] == ".":
                count += 1
        dotcount_h.append(count)
    for i in range(m):
        for j in range(n):
            if picture[j][i] == ".":
                ans = min(dotcount_h[i] + dotcount_w[j] - 1, ans)
            else:
                ans = min(dotcount_h[i] + dotcount_w[j], ans)
    print(ans)
