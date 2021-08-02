n = int(input())
s = [int(q) for q in input()]
a = [list(map(int, input().split())) for _ in range(n)]
d = s[::]
ans = sum(d)
for q in range(1179):
    for q1 in range(len(a)):
        if a[q1][1] <= q and (q - a[q1][1]) % a[q1][0] == 0:
            d[q1] = 1 - d[q1]
    ans = max(ans, sum(d))
print(ans)
