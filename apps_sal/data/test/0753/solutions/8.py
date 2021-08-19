from fractions import gcd


def socr(a, b):
    tmp = gcd(a, b)
    return (a // tmp, b // tmp)


(a, b, c, d) = list(map(int, input().split()))
ans = socr(a * d - b * c, a * d)
(a, b) = (b, a)
(c, d) = (d, c)
ans = socr(a * d - b * c, a * d) if ans[0] < 0 or ans[1] < 0 else ans
print(str(int(ans[0])) + '/' + str(int(ans[1])))
