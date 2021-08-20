n = int(input())
a = [0] * n
(p, q) = (0, 0)
for i in map(int, input().split()):
    if i > p:
        q = p
        p = i - 1
        a[p] -= 1
    elif i > q:
        q = i - 1
        a[p] += 1
print(a.index(max(a)) + 1)
