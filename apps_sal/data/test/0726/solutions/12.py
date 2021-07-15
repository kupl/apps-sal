n, d = map(int, input().split())
a = list(map(int, input().split()))

l = set()
for i in a:
    x = i + d
    r = 100000000000
    for j in a:
        r = min(abs(x - j), r)
    if r == d:
        l.add(x)
    x = i - d
    r = 100000000000
    for j in a:
        r = min(abs(x - j), r)
    if r == d:
        l.add(x)
print(len(l))
