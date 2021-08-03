n = int(input())
a = list(map(int, input().split()))
vis = [False] * 100005
b = []
m = 0
for i in range(n):
    if not vis[i]:
        m += 1
        cur = i
        len = 0
        while not vis[cur]:
            vis[cur] = True
            len += 1
            cur = a[cur] - 1
        b.append(len)
b.sort()
if m > 1:
    b[-2] += b[-1]
    b.pop()
print(sum(map(lambda x: x**2, b)))
