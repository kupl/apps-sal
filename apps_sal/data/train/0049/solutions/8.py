def cnt(l, c):
    if l <= c:
        return 10**c
    res = 1
    if c > 0:
        res += l * 9
    if c > 1:
        res += l * (l - 1) * 9 * 9 // 2
    if c > 2:
        res += l * (l - 1) * (l - 2) * 9 * 9 * 9 // 6
    return res


def calc(n, c):
    x = str(n)
    xn = len(x)
    if xn <= c:
        return n + 1
    res = cnt(xn - 1, c) + 1
    d = int(x[0])
    if d > 1:
        res += cnt(xn - 1, c - 1) * (d - 1)
    if c > 1:
        for i in range(1, xn):
            d = int(x[i])
            if d != 0:
                res += calc(int(x[i:]), c - 1) - 1
                break
    return res


"""ans=0
for i in range(90000):
    s = str(i)
    if len(s)-s.count('0') < 3:
        ans+=1
print(ans)"""

# ans=calc(1000000,3) # 15850
t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    print(calc(r, 3) - calc(l - 1, 3))
