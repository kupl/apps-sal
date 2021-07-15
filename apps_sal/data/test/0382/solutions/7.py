n, m, q = list(map(int, input().split()))
s = list(input())
t = list(input())
a = [list(map(int, input().split())) for i in range(q)]

if n < m:
    for i in range(q):
        print(0)
    return

res = [0] * (n - m + 1)
for i in range(n - m + 1):
    if s[i:(i + m)] == t:
        res[i] = 1

for u in range(q):
    l = a[u][0]
    r = a[u][1]

    ans = 0
    for y in range(l - 1, r - m + 1):
        # print(y)
        if res[y] == 1:
            ans += 1

    print(ans)
