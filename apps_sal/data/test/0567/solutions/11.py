def ii():
    return int(input())
def mi():
    return map(int, input().split())
def li():
    return list(mi())

n = ii()
a = li()
m = 10 ** 6 // 2
x = 0
y = 10 ** 6
for ai in a:
    if ai <= m:
        x = max(x, ai)
    else:
        y = min(y, ai)
ans = max(x - 1, 10 ** 6 - y)
print(ans)
