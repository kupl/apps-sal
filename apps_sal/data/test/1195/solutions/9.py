ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n = ii()
a = li()
ans = 2 + (a[2] ^ min(a))
print(ans)
