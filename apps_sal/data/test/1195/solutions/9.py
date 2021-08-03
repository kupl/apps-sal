def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n = ii()
a = li()
ans = 2 + (a[2] ^ min(a))
print(ans)
