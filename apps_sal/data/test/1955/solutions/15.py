n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = [0] * n
d = {0: 1}
for i in range(n - 1, -1, -1):
    if a[i] not in d:
        s[i] = a[i]
        d[a[i]] = 1

if len(d) != m + 1:
    print(-1)
    return

q = 0
for i in range(n):
    if s[i] == 0:
        q += 1
    else:
        if q >= b[s[i] - 1]:
            q -= b[s[i] - 1]
        else:
            print(-1)
            return


def calc(k):
    s = [0] * k
    d = {0: 1}
    for i in range(k - 1, -1, -1):
        if a[i] not in d:
            s[i] = a[i]
            d[a[i]] = 1

    q = 0
    p = 0
    for i in range(k):
        if s[i] == 0:
            q += 1
        else:
            if q >= b[s[i] - 1]:
                q -= b[s[i] - 1]
                p += 1
            else:
                return False
    if p == m:
        return True
    else:
        return False


l, r = 0, n
while r - l > 1:
    mid = (r + l) // 2
    if calc(mid):
        r = mid
    else:
        l = mid

print(r)
