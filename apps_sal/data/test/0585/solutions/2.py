(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
M = [a[i] for i in range(n)]
for i in range(n - 2, -1, -1):
    M[i] = min(M[i], M[i + 1])
res = 1
mod = 998244353
val = b[m - 1]
id = n - 1
count = m - 1
(l, r) = (-1, -1)
while count and id > -1:
    if M[id] > val:
        id -= 1
    elif M[id] == val:
        if r == -1:
            r = id
        id -= 1
    elif val > M[id]:
        l = id + 1
        res *= max(r - l + 1, 0)
        res %= mod
        count -= 1
        r = -1
        l = -1
        val = b[count]
if count:
    res = 0
    print(res)
else:
    check = min((a[i] for i in range(id + 1)))
    if check == b[0]:
        print(res)
    else:
        print(0)
