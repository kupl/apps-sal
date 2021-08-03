import math
n = int(input())
a = list(map(int, input().split(" ")))
d = 0

count1 = 0
for _ in a:
    d = math.gcd(d, _)
    if _ == 1:
        count1 += 1
if d != 1:
    print(-1)

elif count1 > 0:
    print(n - count1)
else:
    mi = math.inf
    for i in range(len(a) - 1):
        dd = a[i]
        for j in range(i + 1, len(a)):
            dd = math.gcd(dd, a[j])
            if dd == 1:
                mi = min(mi, j - i + n - 1)

    print(mi)
