def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n, m = mi()
a = [[] for i in range(m + 1)]
for i in range(n):
    s, r = mi()
    a[s].append(r)

ch = [0] * (n + 1)
for i in range(1, m + 1):
    a[i].sort(reverse=True)
    pr = 0
    for j in range(len(a[i])):
        pr += a[i][j]
        if pr > 0:
            ch[j + 1] += pr

ans = max(ch)
print(ans)
