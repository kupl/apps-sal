def pw(a, x, k):
    if a == 0:
        return 0
    ans = a
    while k > 0:
        ans *= x
        k = k - 1
    return ans


(n, k, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
lft = []
lft.append(0)
for val in a:
    lft.append(val)
lft.append(0)
rht = []
for val in lft:
    rht.append(val)
for i in range(1, len(lft)):
    lft[i] = lft[i] | lft[i - 1]
for i in range(len(rht) - 2, -1, -1):
    rht[i] = rht[i] | rht[i + 1]
ans = 0
for i in range(1, len(lft) - 1):
    if ans < lft[i - 1] | pw(a[i - 1], x, k) | rht[i + 1]:
        ans = lft[i - 1] | pw(a[i - 1], x, k) | rht[i + 1]
print(ans)
