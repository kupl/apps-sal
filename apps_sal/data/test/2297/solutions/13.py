def getsum(a, b):
    if a % 2 == 0:
        return (a + b) * ((b - a) // 2 + 1) // 2
    else:
        return -(a + b) * ((b - a) // 2 + 1) // 2


q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    if l == r:
        print(l if l % 2 == 0 else -l)
    else:
        print(
            getsum(l if l % 2 == 1 else l + 1, r if r % 2 == 1 else r - 1) +
            getsum(l if l % 2 == 0 else l + 1, r if r % 2 == 0 else r - 1)
        )
