n = int(input())
xy = [list(map(int, input().split()))for _ in range(n)]
g = 39
a = []
if sum(xy[0]) % 2 == 0: a.append(1)
for i in range(g): a.append(1 << i)
g = len(a)
for x, y in xy:
    if (x + y) % 2 != sum(xy[0]) % 2: print(-1); return()
print(g)
print(*a)


def f(s):
    t = s
    ans = []
    for i in a[::-1]:
        if abs(t - i) < abs(t + i):
            ans.append(-i)
            t -= i
        else:
            ans.append(i)
            t += i
    return ans[::-1]


for x, y in xy:
    xpy = f(-(x + y))
    xmy = f(-(x - y))
    ans = ""
    for p, m in zip(xpy, xmy):
        if 0 < p and 0 < m: ans += "R"
        if p < 0 and m < 0: ans += "L"
        if 0 < p and m < 0: ans += "U"
        if p < 0 and 0 < m: ans += "D"
    print(ans)
