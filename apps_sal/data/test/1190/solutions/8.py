ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())

w1, h1, w2, h2 = mi()
ans = h1 + h2 + 2 + w1 + w2 + 2 + h1 + h2 + w1 - w2
print(ans)
