n, x = list(map(int, input().split()))
L = list(map(int, input().split()))
dist = 0
res = 0
for i, l in enumerate(L, 1):
    dist += l
    if dist > x:
        print(i)
        return
    elif dist == x:
        print((i + 1))
        return
print((n + 1))
