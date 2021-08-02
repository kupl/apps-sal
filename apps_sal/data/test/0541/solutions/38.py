n, m = list(map(int, input().split()))
a = []
for _ in range(m):
    b = list(map(int, input().split()))
    a.append(b)

a.sort()

left = a[0][0]
right = a[0][1]

ans = 1

for i in range(1, m):
    x = a[i][0]
    y = a[i][1]

    if left <= x < right:
        left = x
        right = min(right, y)

    else:
        ans += 1
        left = x
        right = y

print(ans)
