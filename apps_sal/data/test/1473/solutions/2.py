n = int(input())
a = {}
b = {}
ans = [0] * n
s = set()
for i in range(n):
    x, y = list(map(int, input().split()))
    a[x] = y
    b[y] = x
    s.add(x)
    s.add(y)
cur = a[0]
for i in range(1, n, 2):
    ans[i] = cur
    if cur in a:
        cur = a[cur]

frst = -1
for i in s:
    if i not in b:
        frst = i
        break
cur = frst
i = 0
for i in range(0, n, 2):
    ans[i] = cur
    if cur in a:
        cur = a[cur]
    
print(*ans)

