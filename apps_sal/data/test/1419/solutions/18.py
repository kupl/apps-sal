n = int(input())
s = input()
lo, hi = 0, 2000000
ans = 1000000
c = 0
l = []
for i in s:
    c += 1
    if i == '-' or i == ' ':
        l.append(c)
        c = 0
l.append(c)


def possible(x):
    rows = 1
    curr = 0
    for i in l:
        if (curr + i) <= x:
            curr += i
        elif i > x:
            return False
        else:
            rows += 1
            curr = i
    return rows <= n


while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(ans)
