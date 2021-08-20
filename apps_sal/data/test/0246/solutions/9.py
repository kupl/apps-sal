(n, s) = map(int, input().split())
mdist = 10 ** 5
c = s
ans = 0


def mySum(c):
    s = str(c)
    ret = 0
    for x in s:
        ret += ord(x) - ord('0')
    return ret


while mdist and c <= n:
    if c - mySum(c) >= s:
        ans += 1
    mdist -= 1
    c += 1
c = min(c, n + 1)
print(ans + n - c + 1)
