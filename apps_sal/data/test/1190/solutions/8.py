def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


w1, h1, w2, h2 = mi()
ans = h1 + h2 + 2 + w1 + w2 + 2 + h1 + h2 + w1 - w2
print(ans)
