
def get(a):
    if (a <= h):
        return a * (a + 1) // 2;
    tmp = a - h + 1;
    re = h * (h - 1) // 2;
    l = (tmp + 1) // 2;
    r = tmp // 2;
    re += l * (h - 1 + l + h) // 2;
    re += r * (h - 1 + r + h) // 2;
    return re;

lo = 1
hi = 1000000000000000001
n, h = list(map(int, input().split()))
while (lo < hi):
    mi = (lo + hi) // 2;
    if (get(mi) < n):
        lo = mi + 1;
    else:
        hi = mi;
print(lo)

