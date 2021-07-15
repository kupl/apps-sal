ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

n = ii()
ans = 0
for i in range(3, n + 1):
    ans += i * (i - 1)
print(ans)
