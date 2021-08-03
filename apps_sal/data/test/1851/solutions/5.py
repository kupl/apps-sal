def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n = ii()
a = li()
i = c = 0
while i < n:
    j = a[i] - 1
    while i < j:
        i += 1
        j = max(j, a[i] - 1)
    c += 1
    i += 1
print(c)
