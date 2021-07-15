n, m = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in range(n):
    s = sum(t[:i])
    li = sorted(t[:i])
    res = 0
    while s > m - t[i]:
        res += 1
        s -= li[-1]
        li.pop()
    print(res, end=" ")
