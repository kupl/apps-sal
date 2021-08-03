def ii(): return int(input())
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


n = ii()
x, y = -1, -1
ans = 0
for _ in range(n):
    a, b = mi()
    if x > y:
        if b >= x:
            ans += 1
            y = x
    elif y > x:
        if a >= y:
            ans += 1
            x = y
    if x == y:
        ans += min(a, b) - x
    x, y = a, b
print(ans)
