n = int(input())
h = list(map(int, input().split()))
view1 = h[0]
view = 0
c = 1
for i in range(1, n):
    if view1 <= h[i] and view <= h[i]:
        c += 1
    view = max(view, h[i])
print(c)
