(n, k, m) = list(map(int, input().split()))
tt = list(map(int, input().split()))
tt.sort()
s = sum(tt)
ans = 0


def check(x, m):
    ret = (k + 1) * x
    m -= s * x
    if m < 0:
        return -1
    for i in range(k):
        if tt[i] * (n - x) <= m:
            m -= tt[i] * (n - x)
            ret += n - x
        else:
            ret += m // tt[i]
            m -= m // tt[i] * tt[i]
        if m <= 0:
            break
    return ret


for i in range(n + 1):
    ans = max(ans, check(i, m))
print(ans)
