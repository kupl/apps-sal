def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n = ii()
ans = 0
for i in range(3, n + 1):
    ans += i * (i - 1)
print(ans)
