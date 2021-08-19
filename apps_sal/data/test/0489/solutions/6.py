def f(n, r):
    if r == 1:
        return n
    elif r == 2:
        return n * (n - 1) // 2
    else:
        return n * (n - 1) * (n - 2) // 6


n = int(input())
a = list(map(int, input().split()))
dic = {}
for ai in a:
    if ai in dic:
        dic[ai] += 1
    else:
        dic[ai] = 1
a = list(sorted(set(a)))
ans = 1
i = 0
cnt = 3
while 0 < cnt:
    x = dic[a[i]]
    if cnt < x:
        ans *= f(x, min(x, cnt))
    cnt -= x
    i += 1
print(ans)
