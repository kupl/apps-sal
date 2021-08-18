n = int(input())
a = list(map(int, input().split()))

s = 0
anse = 0
for i in range(n):
    s += a[i]
    if i % 2 == 0 and s <= 0:
        anse += 1 - s
        s = 1
    elif i % 2 == 1 and s >= 0:
        anse += s + 1
        s = -1

s = 0
anso = 0
for i in range(n):
    s += a[i]
    if i % 2 == 0 and s >= 0:
        anso += s + 1
        s = -1
    elif i % 2 == 1 and s <= 0:
        anso += 1 - s
        s = 1

ans = min(anse, anso)

print(ans)
