def maxd(val):
    mx = 0
    while val > 0:
        mx = max(mx, val % 10)
        val //= 10
    return mx


def mind(val):
    mn = 9
    while val > 0:
        mn = min(mn, val % 10)
        val //= 10
    return mn


t = int(input())
while t > 0:
    t -= 1
    (a, k) = map(int, input().split())
    k -= 1
    while k > 0 and mind(a) > 0:
        a = a + mind(a) * maxd(a)
        k -= 1
    print(a)
