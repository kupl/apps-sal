def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

n, k, m = mi()
s = [''] + input().split()
a = [0] + li()
g = [0] * (k + 1)
p = {}
for i in range(1, k + 1):
    b = li()[1:]
    g[i] = min(a[x] for x in b)
    for x in b: p[s[x]] = i
msg = input().split()
ans = sum(g[p[w]] for w in msg)
print(ans)

