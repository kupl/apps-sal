def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n = ii()
a = li()
m = max(a)
i = 0
ans = 1
while i < n:
    j = i + 1
    while j < n and a[i] == a[j]:
        j += 1
    if a[i] == m:
        ans = max(ans, j - i)
    i = j
print(ans)
