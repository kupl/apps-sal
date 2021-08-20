(n, m, x) = map(int, input().split())
a = list(map(int, input().split()))
p = 0
q = 0
for i in a:
    if i > x:
        p += 1
    elif i < x:
        q += 1
print(min(p, q))
