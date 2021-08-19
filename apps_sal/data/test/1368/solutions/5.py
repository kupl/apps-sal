import math


def C(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


(n, a, b) = map(int, input().split())
l = sorted(list(map(int, input().split())), reverse=True)
print(sum(l[:a]) / a)
if l.count(l[a - 1]) > 1:
    ans = 0
    x = l[a - 1]
    y = l[:a].count(x)
    z = l.count(x)
    if l[0] != x:
        print(C(z, y))
    else:
        ans = 0
        for i in range(a, min(b, z) + 1):
            ans += C(z, i)
        print(ans)
else:
    print(1)
