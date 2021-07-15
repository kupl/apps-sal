ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n = ii()
a = li()
b = [0]
for x in a:
    b.append(b[-1] + x)
mn = min(b)
b = [x - mn + 1 for x in b]
if sorted(b) == list(range(1, n + 1)):
    print(*b)
else:
    print(-1)
