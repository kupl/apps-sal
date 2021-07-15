n,k = map(int, input().split())
a = list(map(int, input().split()))
sm = sum(a)
l,r = -1, 10 ** 20
def check(m):
    return round((sm + k * m) / (n + m) + 0.000001) >= k
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m
print(r)
