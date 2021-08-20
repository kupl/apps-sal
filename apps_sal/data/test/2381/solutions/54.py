(n, k) = list(map(int, input().split()))
a = [int(x) for x in input().split()]
mod = 10 ** 9 + 7
nega = sorted([a[i] for i in range(n) if a[i] < 0], reverse=True)
ans = 1
if k == n:
    for i in a:
        ans *= i
        ans %= mod
elif k % 2 and n == len(nega):
    for i in range(k):
        ans *= nega[i]
        ans %= mod
else:
    a = sorted(a, key=lambda x: abs(x), reverse=True)
    pi = ni = -1
    cnt = 0
    x = []
    for i in range(k):
        x.append(a[i])
        if a[i] < 0:
            ni = i
            cnt += 1
        if a[i] > 0:
            pi = i
    if cnt % 2:
        mx = max(a[k:])
        mn = min(a[k:])
        if abs(a[pi] * mx) <= abs(a[ni] * mn) and pi >= 0:
            x.append(mn)
            x.remove(a[pi])
        else:
            x.append(mx)
            x.remove(a[ni])
    for i in range(k):
        ans *= x[i]
        ans %= mod
print(ans)
