ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n = ii()
a = li()
a.sort(reverse=True)
x, y = [], []
for i in range(1, n):
    (x if i % 2 else y).append(a[i])
ans = x[::-1] + [a[0]] + y
print(*ans)
