n, m = map(int, input().split())
z = set(range(1, m + 1))
for u in range(n):
    x, y = map(int, input().split())
    for i in range(x, y + 1):
        z.discard(i)
print(len(z))
for i in z:
    print(i, end = ' ')

