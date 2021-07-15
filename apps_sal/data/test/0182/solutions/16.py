a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
t, k = 0, 0
for i in range(3):
    t += max(0, a[i] - b[i]) // 2
    if a[i] < b[i]:
        k += b[i] - a[i]
print("Yes" if t >= k else "No")
